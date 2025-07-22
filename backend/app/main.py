from fastapi import FastAPI
from .routes import router

app = FastAPI(
    title="Сервис доставки",
    description="Добавление и получение посылок",
    version="1.0"
)

app.include_router(router)