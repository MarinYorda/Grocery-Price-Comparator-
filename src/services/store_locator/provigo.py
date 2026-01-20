from typing import List
from .base import Store


def find_nearby_stores(lat: float, lon: float, radius_km: float) -> List[Store]:
    return [
        {
            "provider": "provigo",
            "store_id": "provigo-001",
            "name": "Provigo (Demo Store 001)",
            "address": "123 Demo St, Montreal, QC",
            "lat": lat + 0.005,
            "lon": lon - 0.004,
            "distance_km": 1.1,
        }
    ]
