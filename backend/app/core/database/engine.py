"""Движок для подключения к БД и получения сессии."""

from collections.abc import AsyncGenerator
from typing import Any

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

from app.core.config import app_config

engine: AsyncEngine = create_async_engine(app_config.db.url, echo=app_config.DEBUG)
session_maker: async_sessionmaker[AsyncSession] = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_db_session() -> AsyncGenerator[AsyncSession, Any]:
    """
    Получение сессии подключения к БД.

    Yields:
        AsyncSession: Сессия подключения к БД.

    Examples:
        >>> from fastapi import FastAPI, Depends
        >>>
        >>> app = FastAPI()
        >>>
        >>> @app.get("/")
        >>> async def example(db_session: AsyncSession = Depends(get_async_db_session)):
        ...     pass
    """
    async with session_maker() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            if session.is_active:
                await session.rollback()
            raise
