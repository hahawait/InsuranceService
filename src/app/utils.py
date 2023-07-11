"""Вспомагательные функции"""
import json
from datetime import datetime
from .models import Tariff


async def load_tariffs_from_json(file_path):
    """Загружает датку из json файла"""
    with open(file_path, 'r') as file:
        data = json.load(file)

    for date_str, tariffs in data.items():
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        for tariff_data in tariffs:
            cargo_type = tariff_data['cargo-type']
            rate = float(tariff_data['rate'])
            await Tariff.create(date=date, cargo_type=cargo_type, rate=rate)
