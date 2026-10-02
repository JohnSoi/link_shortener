from fastapi import FastAPI

app: FastAPI = FastAPI(title="LinkShortener", description="LinkShortener_Backend")


@app.get("/health", description="Проверка состояния приложения")
def health_check() -> dict:
    return {"status": "ok"}
