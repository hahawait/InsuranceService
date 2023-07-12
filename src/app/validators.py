from typing import Dict, List
from pydantic import BaseModel


class CargoItem(BaseModel):
    cargo_type: str
    rate: float


class TariffData(BaseModel):
    tariff_data: Dict[str, List[CargoItem]]
