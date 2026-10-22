"""Модель пользователя."""

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.core import DEFAULT_STRING_LENGTH
from app.core.database import BaseModel, DatetimeMixin


class UserModel(BaseModel, DatetimeMixin):
    """
    Модель пользователя.

    Attributes:
        email (str): Электронная почта пользователя.
        password_hash (str): Хэш пароля пользователя.
    """

    __tablename__ = "users"

    _PROTECTED_FIELDS = ("password_hash",)

    email: Mapped[str] = mapped_column(String(DEFAULT_STRING_LENGTH), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(DEFAULT_STRING_LENGTH), nullable=False)
