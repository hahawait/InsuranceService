"""Бизнес-логика"""
from .models import Tariff


async def calculate_insurance_cost(date, cargo_type, declared_value):
    """Возвращает стоимость страхования для актуального тарифа"""
    tariff = await Tariff.filter(date=date, cargo_type=cargo_type).first()
    return declared_value * float(tariff.rate)
