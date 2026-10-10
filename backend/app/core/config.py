from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class DatabaseConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
        env_prefix="DB_"
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
        return f"{self.TYPE}+{self.ENGINE}://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.NAME}"


class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
        env_prefix="APP_"
    )

    db: DatabaseConfig = DatabaseConfig()

    NAME: str
    DESCRIPTION: str
    VERSION: str
    ENV: Literal["dev", "prod", "test"] = "prod"
    DEBUG: bool = False


app_config: AppConfig = AppConfig()
