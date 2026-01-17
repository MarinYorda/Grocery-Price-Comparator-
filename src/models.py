from typing import Optional
from pydantic import BaseModel, field_validator, computed_field

class Product(BaseModel):
    store: str
    name: str
    category: Optional[str] = None
    price: float
    quantity: float
    unit: str

    @field_validator("store", "name", "unit", "category", mode="before")
    @classmethod
    def strip_strings(cls, v):
        if v is None:
            return v
        return str(v).strip()

    @field_validator("unit")
    @classmethod
    def validate_unit(cls, v):
        v = v.lower()
        if v not in {"g", "ml"}:
            raise ValueError(f"Invalid unit: {v}")
        return v
    
    @field_validator("price", "quantity")
    @classmethod
    def must_be_positive(cls,v):
        if v <= 0:
            raise ValueError("Must be greater than 0")
        return v
    
    # --- Computed fields --- -> normalization of data to have price per 100g or 100ml that will then enable easier checks in future price comparisons 
    @computed_field
    @property
    def price_per_100(self) -> float:
        """
        Normalized price per 100g or 100ml
    
        """
        return round((self.price / self.quantity) * 100, 2)
    
    @computed_field
    @property
    def normalized_unit(self) -> str:
        return "100g" if self.unit == "g" else "100ml"

