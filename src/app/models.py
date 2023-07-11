"""Модели приложения"""
from tortoise.models import Model
from tortoise import fields


class Tariff(Model):
    """Модель тарифа"""

    date = fields.DateField()
    cargo_type = fields.CharField(max_length=100)
    rate = fields.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        """Название таблицы в бд"""
        table = "tariffs"
