"""Утилиты для работы с доступом."""

from datetime import UTC, datetime, timedelta
from typing import Any

from jose import jwt
from passlib.context import CryptContext

from app.core import app_config

# Контекст для шифрования паролей.
pwd_context: CryptContext = CryptContext(
    schemes=["argon2"],
    deprecated="auto",
)


def hash_password(password: str) -> str:
    """
    Хеширование пароля.

    Args:
        password (str): Пароль для хеширования.

    Returns:
        str: Хешированный пароль.

    Example:
        >>> from app.core.access import hash_password
        >>> hash_password("password")  # "hashed_password"
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Проверка валидности пароля с помощью хешированного.

    Args:
        plain_password (str): Пароль для проверки.
        hashed_password (str): Хешированный пароль.

    Returns:
        bool: Корректен ли пароль.

    Example:
        >>> from app.core.access import verify_password, hash_password
        >>> hashed_pass: str = hash_password("password")
        >>> verify_password("password", hashed_pass)  # True
        >>> verify_password("password1", hashed_pass)  # False
    """
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(token_data: dict[str, Any], expires_delta: timedelta | None = None) -> str:
    """
    Создание JWT токена для аутентификации.

    Args:
        token_data (dict[str, Any]): Данные для токена.
        expires_delta (timedelta | None): Время жизни токена.
            По умолчанию app_config.access.TOKEN_EXPIRES_IN_MINUTES минут.

    Returns:
        str: JWT токен.

    Example:
        >>> from app.core.access import create_access_token
        >>> create_access_token({"sub": "user_id"})  # JWT токен
    """
    to_encode: dict[str, Any] = token_data.copy()
    expire: datetime = datetime.now(UTC) + (
        expires_delta or timedelta(minutes=app_config.access.TOKEN_EXPIRES_IN_MINUTES)
    )
    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, app_config.access.SECRET, algorithm=app_config.access.JWT_ALGORITHM)


def decode_access_token(token: str) -> dict[str, Any]:
    """
    Декодирование JWT токена.

    Args:
        token (str): JWT токен.

    Returns:
        dict[str, Any]: Декодированные данные токена.

    Example:
        >>> from app.core.access import create_access_token, decode_access_token
        >>> jwt_token: str = create_access_token({"sub": "user_id"})  # JWT токен
        >>> decode_access_token(jwt_token)  # {"sub": "user_id"}
    """
    return jwt.decode(token, app_config.access.SECRET, algorithms=[app_config.access.JWT_ALGORITHM])
