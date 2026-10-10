from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
        env_prefix="APP_"
    )

    NAME: str
    DESCRIPTION: str
    VERSION: str
    ENV: Literal["dev", "prod", "test"] = "prod"
    DEBUG: bool = False


app_config: AppConfig = AppConfig()
