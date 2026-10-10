from fastapi import FastAPI

from app.core import app_config

app: FastAPI = FastAPI(
    title=app_config.NAME,
    description=app_config.DESCRIPTION,
    version=app_config.VERSION,
    debug=app_config.DEBUG,
)


@app.get("/health", description="Проверка состояния приложения")
def health_check() -> dict:
    return {"status": "ok"}
