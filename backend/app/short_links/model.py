"""Модель для работы с короткими ссылками."""

from datetime import datetime

from sqlalchemy import ForeignKey, Index, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core import DEFAULT_STRING_LENGTH
from app.core.database import BaseModel, DatetimeMixin


class ShortLinkModel(BaseModel, DatetimeMixin):
    """
    Модель для работы с короткими ссылками.

    Attributes:
        user_id: ID пользователя, создавшего ссылку.
        original_url: Оригинальная ссылка.
        normalize_url: Нормализованная ссылка.
        short_code: Короткая ссылка.
        click_count: Количество кликов на ссылку.
        last_accessed_at: Дата последнего доступа к ссылке.
    """

    __tablename__: str = "short_links"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=True)
    original_url: Mapped[str] = mapped_column(String(DEFAULT_STRING_LENGTH), nullable=False)
    normalize_url: Mapped[str] = mapped_column(String(DEFAULT_STRING_LENGTH), nullable=False)
    short_code: Mapped[str] = mapped_column(String(10), unique=True, index=True, nullable=False)
    click_count: Mapped[int] = mapped_column(default=0, nullable=False)
    last_accessed_at: Mapped[datetime] = mapped_column(server_default=func.now(), default=func.now())

    __table_args__ = (Index("idx_unique_links", func.coalesce(user_id, -1), original_url, unique=True),)
