from fastapi import APIRouter
from .service import calculate_insurance_cost

router = APIRouter()


@router.post("/insurance-cost")
async def calculate_insurance(date: str, cargo_type: str, declared_value: float):
    insurance_cost = await calculate_insurance_cost(date, cargo_type, declared_value)
    return {"insurance_cost": insurance_cost}
