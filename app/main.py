from fastapi import FastAPI
from app.config import get_settings
from app.routers import movements
from fastapi.middleware.cors import CORSMiddleware

settings=get_settings()

app = FastAPI(
    title="Budjetame",
    openapi_url="/openapi.json",
    swagger_ui_parameters={"docExpansion": "none"}
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(movements.router)

