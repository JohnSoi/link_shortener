"""Роуты для работы с пользователями и доступом."""

from fastapi import APIRouter, Depends

from .dependencies import get_user_service
from .schemas import UserAccessData, UserRegisterData
from .service import UserService

access_routes: APIRouter = APIRouter(prefix="/user", tags=["user"])


@access_routes.post("/register", description="Регистрация нового пользователя", response_model=UserAccessData)
async def register_user(
    payload: UserRegisterData,
    user_service: UserService = Depends(get_user_service),  # noqa: B008
) -> UserAccessData:
    """Регистрация нового пользователя."""
    return await user_service.register(payload)
