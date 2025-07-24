from fastapi import FastAPI
from app.routers import movements

app = FastAPI(
    title="Budjetame",
    openapi_url="/openapi.json",
    swagger_ui_parameters={"docExpansion": "none"}
)

app.include_router(movements.router)

