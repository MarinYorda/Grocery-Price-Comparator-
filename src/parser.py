from typing import List, Union
from pydantic import ValidationError
from src.models import Product

def parse_product(product: dict) -> dict:
    return Product.model_validate(product).model_dump()

def parse_products(products: list[dict]) -> list[dict]:
    return [Product.model_validate(p).model_dump() for p in products]



# # Parse a single product 
# def parse_product(product: Dict) -> Dict:
#     parsed_info = {}
    
#     required_keys = ["name", "price", "quantity", "unit", "store"]

#     for key in required_keys:
#         if key not in product:
#             raise ValueError(f"Missing required key: {key}")
    
#     # Store
#     store = str(product["store"]).strip()
#     parsed_info["store"] = store
    
#     # Name
#     name = str(product["name"]).strip()
#     parsed_info["name"] = name

#     # Category
#     raw_category = product.get("category")
#     category = str(raw_category).strip() if raw_category is not None else None
#     parsed_info["category"] = category

#     # Price
#     price = float(product["price"])
#     parsed_info["price"] = price

#     # Quantity
#     quantity = float(product["quantity"])
#     parsed_info["quantity"] = quantity

#     # Unit
#     unit = str(product["unit"]).strip().lower() 
#     allowed_units = ["g", "ml"]
#     if unit not in allowed_units:
#         raise ValueError(f"The following units are wrong: {unit}")
#     parsed_info["unit"] = unit

#     return parsed_info

# def parse_products(products: list[Dict]) -> list[Dict]:
#     final_product_list = []
#     for product in products:
#         final_product_list.append(parse_product(product))

#     return final_product_list
