from typing import List, Union
from pydantic import ValidationError
from src.models import Product

def parse_product(product: dict) -> dict:
    return Product.model_validate(product).model_dump()

def parse_products(products: list[dict]) -> list[dict]:
    return [Product.model_validate(p).model_dump() for p in products]

