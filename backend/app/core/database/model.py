"""Базовая модель."""

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class BaseModel(DeclarativeBase):
    """
    Базовая модель приложения.

    Notes:
        Абстрактная базовая модель для всех моделей приложения.

    Attributes:
        id (int): Идентификатор записи.

    Methods:
        to_dict(): Преобразует объект в словарь.

    Examples:
        >>> from app.core.database import BaseModel
        >>>
        >>> # Модель пользователя с именем таблицы "user"
        >>> class User(BaseModel):
        ...     __tablename__ = "users"
        ...     name: str = mapped_column()
        >>>
        >>>
        >>> # Модель действия пользователя с именем таблицы "user_action"
        >>> class UserAction(BaseModel):
        ...     __tablename__ = "user_action"
        ...     user_id: int = mapped_column()
    """

    __abstract__: bool = True

    _PROTECTED_FIELDS: tuple[str, ...] = ()

    id: Mapped[int] = mapped_column(primary_key=True)

    def to_dict(self) -> dict:
        """
        Преобразует объект в словарь.

        Returns:
            dict: Словарь с атрибутами объекта.
        """
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
            if column.name not in self._PROTECTED_FIELDS
        }

    def __repr__(self) -> str:
        """Строковое представление объекта."""
        return f"<{self.__class__.__name__} {self.id}>"
