from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import app_config
from app.core.database import get_async_db_session

app: FastAPI = FastAPI(
    title=app_config.NAME,
    description=app_config.DESCRIPTION,
    version=app_config.VERSION,
    debug=app_config.DEBUG,
)


@app.get("/health", description="Проверка состояния приложения")
async def health_check(async_db_session: AsyncSession = Depends(get_async_db_session)) -> dict:
    params: dict = {"status": "ok", "debug": app_config.DEBUG}

    if app_config.DEBUG:
        db_check_query =await async_db_session.execute(text("SELECT 1"))

        params.update(
            {
                "db_url": app_config.db.url,
                "db_connected": db_check_query.scalar() == 1,
            }
        )

    return params
