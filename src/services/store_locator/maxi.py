from typing import List
from .base import Store


def find_nearby_stores(lat: float, lon: float, radius_km: float) -> List[Store]:
    return [
        {
            "provider": "maxi",
            "store_id": "maxi-001",
            "name": "Maxi (Demo Store 001)",
            "address": "456 Demo Ave, Montreal, QC",
            "lat": lat - 0.003,
            "lon": lon + 0.006,
            "distance_km": 1.6,
        }
    ]
