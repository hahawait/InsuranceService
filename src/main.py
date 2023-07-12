from fastapi import FastAPI
from database import setup_database
from app.endpoints import router

app = FastAPI()

setup_database(app)

app.include_router(router)
