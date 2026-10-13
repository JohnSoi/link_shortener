"""Базовая модель."""

import re

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from app.core.database.consts import CAMEL_CASE_ABBR_REGEX, CAMEL_CASE_REGEX, REPLACE_PATTERN


class BaseModel(DeclarativeBase):
    """
    Базовая модель приложения.

    Notes:
        Абстрактная базовая модель для всех моделей приложения.
        Самостоятельно формирует имя таблицы на основе имени класса.
        Если необходимо переопределить имя таблицы, можно использовать метод __tablename__.

    Attributes:
        id (int): Идентификатор записи.

    Methods:
        to_dict(): Преобразует объект в словарь.

    Examples:
        >>> from app.core.database import BaseModel
        >>>
        >>> # Модель пользователя с именем таблицы "user"
        >>> class User(BaseModel):
        ...     name: str = mapped_column()
        >>>
        >>>
        >>> # Модель действия пользователя с именем таблицы "user_action"
        >>> class UserAction(BaseModel):
        ...     user_id: int = mapped_column()
        >>>
        >>>
        >>> # Модель действия пользователя c переопределенным именем таблицы "actions"
        >>> class Action(BaseModel):
        ...     __tablename__: str = "actions"
        >>>
    """

    __abstract__: bool = True

    id: Mapped[int] = mapped_column(primary_key=True)

    def to_dict(self) -> dict:
        """
        Преобразует объект в словарь.

        Returns:
            dict: Словарь с атрибутами объекта.
        """
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    @classmethod
    def __tablename__(cls) -> str:
        """Название таблицы из имени класса."""
        s1: str = re.sub(CAMEL_CASE_REGEX, REPLACE_PATTERN, cls.__name__)
        s2: str = re.sub(CAMEL_CASE_ABBR_REGEX, REPLACE_PATTERN, s1)
        return s2.lower()

    def __repr__(self) -> str:
        """Строковое представление объекта."""
        return f"<{self.__class__.__name__} {self.id}>"
