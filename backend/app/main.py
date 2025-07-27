from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor


from otel_setup import setup_tracer
from routes import router

app = FastAPI(
    title="Delivery Service",
    version="1.0.0",
)
setup_tracer("delivery-backend")
FastAPIInstrumentor.instrument_app(app)
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