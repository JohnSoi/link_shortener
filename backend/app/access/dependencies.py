"""Зависимости для работы с доступом и пользователями."""

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_async_db_session

from .service import UserService


def get_user_service(async_session: AsyncSession = Depends(get_async_db_session)) -> UserService:  # noqa: B008
    """
    Зависимость для получения сервиса работы с пользователями.

    Args:
        async_session (AsyncSession): Сессия для работы с БД.

    Returns:
        UserService: Сервис работы с пользователями.

    Examples:
        >>> from fastapi import APIRouter
        >>> access_routes: APIRouter = APIRouter(prefix="/user", tags=["user"])
        >>> @access_routes.post("/")
        >>> async def register_user(payload: dict, user_service: UserService = Depends(get_user_service)) -> dict: ...
    """
    return UserService(async_session)
