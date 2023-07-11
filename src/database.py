"""Конфиг бд"""
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise


def setup_database(app: FastAPI):
    """Настройка для fastapi приложения"""
    register_tortoise(
        app,
        db_url='sqlite://db.sqlite3',
        modules={'models': ['app.models']},
        generate_schemas=True,
        add_exception_handlers=True
    )
