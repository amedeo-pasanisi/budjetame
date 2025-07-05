from fastapi import FastAPI
from .routers import movements

app = FastAPI()

app.include_router(movements.router)

