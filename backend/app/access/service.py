"""Сервис для работы с пользователями и доступом."""

from sqlalchemy.ext.asyncio import AsyncSession

from .repository import UserRepository
from .schemas import UserAccessData, UserRegisterData


class UserService:
    """
    Сервис для работы с пользователями и доступом.

    Attributes:
        _repository (UserRepository): Репозиторий для работы с пользователями.
    """

    _repository: UserRepository

    def __init__(self, async_session: AsyncSession) -> None:
        """
        Инициализация репозитория.

        Args:
            async_session (AsyncSession): Сессия для работы с БД.
        """
        self._repository = UserRepository(async_session)

    async def register(self, payload: UserRegisterData) -> UserAccessData:
        """
        Регистрация пользователя.

        Args:
            payload (UserRegisterData): Данные для регистрации.

        Returns:
            UserAccessData: Данные для доступа.
        """
        result: dict[str, str] = await self._repository.register(payload.email, payload.password)

        return UserAccessData(access_token=result["access_token"])
