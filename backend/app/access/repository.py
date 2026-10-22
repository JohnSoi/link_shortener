"""Репозиторий для работы с пользователями."""

from collections.abc import Sequence
from typing import Any

from fastapi import HTTPException
from sqlalchemy import Result, Row, Select, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.access import create_access_token, hash_password

from .model import UserModel


class UserRepository:
    """
    Репозиторий для работы с пользователями.

    Attributes:
        _MODEL (UserModel): Модель пользователя.
    """

    _MODEL: type[UserModel] = UserModel

    def __init__(self, async_session: AsyncSession) -> None:
        """
        Инициализация репозитория.

        Args:
            async_session (AsyncSession): Сессия для работы с БД.
        """
        self._async_session: AsyncSession = async_session

    async def register(self, email: str, password: str) -> dict[str, str]:
        """
        Регистрация пользователя.

        Args:
            email (str): Email пользователя.
            password (str): Пароль пользователя.

        Returns:
            dict[str, str]: Данные для авторизации.

        Raises:
            HTTPException (400): Если пользователь с данным email уже существует.
        """
        if await self.get_user_by_email(email):
            raise HTTPException(status_code=400, detail="Пользователь с данным email уже существует")

        user_data: UserModel = await self.create(
            {
                "email": email,
                "password_hash": hash_password(password),
            }
        )

        return {"access_token": create_access_token({"sub": user_data.id})}

    async def get_user_by_email(self, email: str) -> Row[UserModel] | None:
        """
        Получение пользователя по email.

        Args:
            email (str): Email пользователя.

        Returns:
            Row[UserModel] | None: Пользователь, если найден.
        """
        users: Sequence[Row[UserModel]] | None = await self.get_by_filters(email=email)

        if not users:
            return None

        return users[0]

    async def get_by_filters(self, **filters) -> Sequence[Row[UserModel]] | None:
        """
        Получение пользователей по фильтрам.

        Args:
            **filters: Фильтры для поиска пользователей.

        Returns:
            Sequence[Row[UserModel]] | None: Пользователи, если найдены.
        """
        query: Select = select(self._MODEL).filter_by(**filters)
        result: Result[UserModel] = await self._async_session.execute(query)

        return result.fetchall()

    async def create(self, data: dict[str, Any]) -> UserModel:
        """
        Создание нового пользователя.

        Args:
            data (dict[str, Any]): Данные пользователя для создания.

        Returns:
            UserModel: Созданный пользователь.
        """
        new_model: UserModel = self._MODEL()

        for key, value in data.items():
            if hasattr(new_model, key):
                setattr(new_model, key, value)

        self._async_session.add(new_model)
        await self._async_session.commit()
        await self._async_session.refresh(new_model)

        return new_model
