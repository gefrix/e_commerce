from __future__ import annotations

import json
from pathlib import Path
from typing import Any, TypeAlias, cast

from src.category import Category
from src.product import Product

JsonObject: TypeAlias = dict[str, Any]


def read_json(file_path: str | Path) -> list[JsonObject]:
    """Read category and product data from a UTF-8 JSON file."""
    path = Path(file_path)
    with path.open("r", encoding="utf-8") as file:
        data: object = json.load(file)

    if not isinstance(data, list):
        raise ValueError("The JSON root element must be a list of categories")

    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Every category in the JSON file must be an object")

    return cast(list[JsonObject], data)


def create_objects_from_json(data: list[JsonObject]) -> list[Category]:
    """Convert raw JSON-compatible data to Category and Product objects."""
    categories: list[Category] = []

    for category_data in data:
        raw_products = category_data.get("products")
        if not isinstance(raw_products, list):
            raise ValueError("The category field 'products' must be a list")

        products: list[Product] = []
        for product_data in raw_products:
            if not isinstance(product_data, dict):
                raise ValueError("Every product in the JSON file must be an object")

            products.append(
                Product(
                    name=str(product_data["name"]),
                    description=str(product_data["description"]),
                    price=float(product_data["price"]),
                    quantity=int(product_data["quantity"]),
                )
            )

        categories.append(
            Category(
                name=str(category_data["name"]),
                description=str(category_data["description"]),
                products=products,
            )
        )

    return categories


def load_categories_from_json(file_path: str | Path) -> list[Category]:
    """Read a JSON file and return fully initialized category objects."""
    return create_objects_from_json(read_json(file_path))
