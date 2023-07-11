from fastapi import FastAPI
from database import setup_database
from app.utils import load_tariffs_from_json
from app.endpoints import router

app = FastAPI()

setup_database(app)


@app.on_event("startup")
async def startup_event():
    await load_tariffs_from_json('tariffs.json')


app.include_router(router)
