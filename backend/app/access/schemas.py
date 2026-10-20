"""Схемы данных пользователей и доступа."""

from pydantic import BaseModel, EmailStr, Field

from app.core import DEFAULT_STRING_LENGTH
from app.core.access import MIN_EMAIL_LENGTH, MIN_PASSWORD_LENGTH


class UserRegisterData(BaseModel):
    """
    Схема данных для регистрации пользователя.

    Attributes:
        email (EmailStr): Электронная почта пользователя.
            Обязательное поле, минимальная длина MIN_EMAIL_LENGTH символа.
        password (str): Пароль пользователя.
            Обязательное поле, минимальная длина MIN_PASSWORD_LENGTH символов.
    """

    email: EmailStr = Field(
        ...,
        examples=["test@test.com"],
        description="Email пользователя",
        min_length=MIN_EMAIL_LENGTH,
        max_length=DEFAULT_STRING_LENGTH,
    )
    password: str = Field(
        ..., min_length=MIN_PASSWORD_LENGTH, max_length=DEFAULT_STRING_LENGTH, description="Пароль пользователя"
    )


class UserAccessData(BaseModel):
    """
    Схема данных для доступа пользователя.

    Attributes:
        access_token (str): Токен доступа пользователя.
    """

    access_token: str = Field(..., description="Токен доступа")
