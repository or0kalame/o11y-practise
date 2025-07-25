from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
from routes import router

app = FastAPI(
    title="Delivery Service",
    version="1.0.0",
)

Instrumentator().instrument(app).expose(app)

# Разрешаем фронтенду доступ
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем маршруты
app.include_router(router)
