from typing import List
from .base import Store


def find_nearby_stores(lat: float, lon: float, radius_km: float) -> List[Store]:
    return [
        {
            "provider": "iga",
            "store_id": "iga-001",
            "name": "IGA (Demo Store 001)",
            "address": "101 Demo Rd, Montreal, QC",
            "lat": lat - 0.012,
            "lon": lon - 0.001,
            "distance_km": 3.0,
        }
    ]
