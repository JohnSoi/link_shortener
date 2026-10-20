"""Модуль для создания FastAPI приложения."""

from typing import Self

from fastapi import APIRouter, Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from .config import app_config
from .database import get_async_db_session


class AppCreator:
    """Класс-билдер для создания FastAPI приложения."""

    def __init__(self) -> None:
        self._app: FastAPI = FastAPI(
            title=app_config.NAME,
            description=app_config.DESCRIPTION,
            version=app_config.VERSION,
            debug=app_config.DEBUG,
        )

    def get_app(self) -> FastAPI:
        """
        Получение FastAPI приложения под собранную конфигурацию.

        Returns:
            FastAPI: FastAPI приложение.

        Examples:
            >>> # Создание FastAPI приложения с GET-маршрутом для проверки состояния приложения.
            >>> app = AppCreator().add_health_routes().get_app()
        """
        return self._app

    def add_health_routes(self) -> Self:
        """
        Добавление GET-маршрута для проверки состояния приложения.

        Returns:
            Self: Экземпляр класса AppCreator.

        Examples:
            >>> # Создание FastAPI приложения с GET-маршрутом для проверки состояния приложения.
            >>> app = AppCreator().add_health_routes().get_app()
        """
        health_router: APIRouter = APIRouter()
        health_router.add_api_route(
            "/health", self.__health_check, methods=["GET"], description="Проверка состояния приложения"
        )
        self._app.include_router(health_router)

        return self

    def include_routers(self, routers: list[APIRouter]) -> Self:
        """
        Добавление списка роутеров в приложение.

        Args:
            routers (list[APIRouter]): Список роутеров.

        Returns:
            Self: Экземпляр класса AppCreator.

        Examples:
            >>> from fastapi import APIRouter
            >>> user_router: APIRouter = APIRouter()
            >>> access_router: APIRouter = APIRouter()
            >>> # Создание FastAPI приложения с добавленными роутерами пользователей и доступа.
            >>> app = AppCreator().include_routers([user_router, access_router]).get_app()
        """
        for router in routers:
            self._app.include_router(router)

        return self

    @staticmethod
    async def __health_check(async_db_session: AsyncSession = Depends(get_async_db_session)) -> dict:  # noqa: B008
        """
        Маршрут для проверки состояния приложения.

        Args:
            async_db_session (AsyncSession): Сессия для подключения к БД.

        Returns:
            dict: Статус работы приложения.
        """
        params: dict = {"status": "ok", "debug": app_config.DEBUG}

        if app_config.DEBUG:
            db_check_query = await async_db_session.execute(text("SELECT 1"))

            params.update(
                {
                    "db_url": app_config.db.url,
                    "db_connected": db_check_query.scalar() == 1,
                }
            )

        return params
