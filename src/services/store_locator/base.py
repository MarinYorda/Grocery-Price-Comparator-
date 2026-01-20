from typing import TypedDict

class Store(TypedDict):
    provider: str
    store_id: str
    name: str
    address: str
    lat: float
    lon: float
    distance_km: float