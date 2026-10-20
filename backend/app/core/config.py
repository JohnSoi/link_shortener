"""Конфиги приложения."""

from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class DatabaseConfig(BaseSettings):
    """
    Конфиг для работы с БД.

    Notes:
        Все параметры в .env файле должны начинаться с DB_.

    Attributes:
        NAME: Имя БД.
        HOST: Хост БД.
        PORT: Порт БД.
        USER: Пользователь БД.
        PASSWORD: Пароль БД.
        TYPE: Тип БД.
    """

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env", env_file_encoding="utf-8", extra="ignore", env_prefix="DB_"
    )

    NAME: str = "link_shortener_db"
    HOST: str = "localhost"
    PORT: int = 5432
    USER: str
    PASSWORD: str
    TYPE: str = "postgresql"
    ENGINE: str = "asyncpg"

    @property
    def url(self) -> str:
        """
        Адрес для подключения к БД.

        Returns:
            str: Адрес для подключения к БД.
        """
        return f"{self.TYPE}+{self.ENGINE}://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.NAME}"


class AccessConfig(BaseSettings):
    """
    Конфиг доступа в приложение.

    Attributes:
        TOKEN_EXPIRES_IN_MINUTES: Время жизни токена в минутах.
        SECRET: Секретный ключ для генерации токена.
        JWT_ALGORITHM: Алгоритм для генерации токена.
    """

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env", env_file_encoding="utf-8", extra="ignore", env_prefix="ACCESS_"
    )

    TOKEN_EXPIRES_IN_MINUTES: int = 30
    SECRET: str
    JWT_ALGORITHM: str = "HS256"


class AppConfig(BaseSettings):
    """
    Конфиг приложения.

    Notes:
        Все параметры в .env файле должны начинаться с APP_.

    Attributes:
        NAME: Имя приложения.
        DESCRIPTION: Описание приложения.
        VERSION: Версия приложения.
        ENV: Окружение приложения.
        DEBUG: Режим отладки.
    """

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env", env_file_encoding="utf-8", extra="ignore", env_prefix="APP_"
    )

    db: DatabaseConfig = DatabaseConfig()  # type: ignore
    access: AccessConfig = AccessConfig()  # type: ignore

    NAME: str
    DESCRIPTION: str
    VERSION: str
    ENV: Literal["dev", "prod", "test"] = "prod"
    DEBUG: bool = False


app_config: AppConfig = AppConfig()  # type: ignore
