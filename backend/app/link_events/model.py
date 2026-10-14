"""Модель события перехода по ссылке."""

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core import DEFAULT_STRING_LENGTH
from app.core.database import BaseModel, DatetimeMixin


class LinkEventModel(BaseModel, DatetimeMixin):
    """
    Модель события перехода по ссылке.

    Attributes:
        link_id: ID ссылки.
        ip_address: IP-адрес пользователя.
        user_agent: User Agent пользователя.
        referer: Реферер пользователя.
    """

    __tablename__ = "link_events"

    link_id: Mapped[int] = mapped_column(
        ForeignKey("short_links.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False
    )
    ip_address: Mapped[str] = mapped_column(String(DEFAULT_STRING_LENGTH), nullable=False)
    user_agent: Mapped[str] = mapped_column(String(DEFAULT_STRING_LENGTH), nullable=False)
    referer: Mapped[str] = mapped_column(String(DEFAULT_STRING_LENGTH), nullable=False)
