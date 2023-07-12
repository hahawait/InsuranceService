from fastapi import APIRouter, HTTPException
from pydantic import ValidationError

from .service import calculate_insurance_cost
from .validators import TariffData
from .models import Tariff


router = APIRouter()


@router.post("/insurance-cost")
async def calculate_insurance(date: str, cargo_type: str, declared_value: float):
    """Возвращает стоимость страхования"""
    insurance_cost = await calculate_insurance_cost(date, cargo_type, declared_value)
    return {"insurance_cost": insurance_cost}


@router.post("/tariff/add")
async def add_tariffs(tariffs_data: TariffData):
    """Добавляет тариф в бд"""
    try:
        for date in tariffs_data.tariff_data:
            for item in tariffs_data.tariff_data[date]:
                new_tariff = await Tariff.create(
                    date=date,
                    cargo_type=item.cargo_type,
                    rate=item.rate
                )
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))
