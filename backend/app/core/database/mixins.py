# pylint: disable=too-few-public-methods
"""Миксины моделей."""

from datetime import datetime

from sqlalchemy import text, func
from sqlalchemy.orm import Mapped, mapped_column


class DatetimeMixin:
    """
    Миксин для моделей с метками времени создания и обновления.

    Attributes:
        created_at (datetime): Дата и время создания записи.
        updated_at (datetime): Дата и время последнего обновления записи.

    Methods:
        is_created (bool): Проверяет, была ли запись создана.
    """

    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now,
        nullable=False,
        server_default=func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.now,
        nullable=False,
        server_default=func.now(),
        onupdate=func.now()
    )

    @property
    def is_created(self) -> bool:
        """
        Проверяет, была ли запись создана.

        Returns:
            bool: True, если запись была создана, False - обновлена.
        """
        return self.created_at == self.updated_at
