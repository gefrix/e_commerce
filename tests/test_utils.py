from __future__ import annotations

import json
from pathlib import Path

import pytest

from src.category import Category
from src.product import Product
from src.utils import create_objects_from_json, load_categories_from_json, read_json

PROJECT_ROOT = Path(__file__).resolve().parents[1]
PRODUCTS_PATH = PROJECT_ROOT / "data" / "products.json"


def test_read_json_returns_category_data() -> None:
    data = read_json(PRODUCTS_PATH)

    assert len(data) == 2
    assert data[0]["name"] == "Смартфоны"
    assert len(data[0]["products"]) == 3


def test_create_objects_from_json_builds_domain_objects() -> None:
    categories = create_objects_from_json(read_json(PRODUCTS_PATH))

    assert len(categories) == 2
    assert all(isinstance(category, Category) for category in categories)
    assert all(isinstance(product, Product) for category in categories for product in category._Category__products)
    assert categories[0]._Category__products[0].name == "Samsung Galaxy C23 Ultra"
    assert categories[1]._Category__products[0].price == 123000.0
    assert Category.category_count == 2
    assert Category.product_count == 4


def test_load_categories_from_json_combines_reading_and_conversion() -> None:
    categories = load_categories_from_json(PRODUCTS_PATH)

    assert [category.name for category in categories] == ["Смартфоны", "Телевизоры"]
    assert [category.products.count("Остаток:") for category in categories] == [3, 1]


def test_read_json_rejects_non_list_root(tmp_path: Path) -> None:
    file_path = tmp_path / "invalid.json"
    file_path.write_text('{"name": "not a list"}', encoding="utf-8")

    with pytest.raises(ValueError, match="root element"):
        read_json(file_path)


def test_read_json_rejects_non_object_category(tmp_path: Path) -> None:
    file_path = tmp_path / "invalid-category.json"
    file_path.write_text(json.dumps(["category"]), encoding="utf-8")

    with pytest.raises(ValueError, match="category"):
        read_json(file_path)


def test_create_objects_rejects_invalid_products_field() -> None:
    with pytest.raises(ValueError, match="products"):
        create_objects_from_json([{"name": "Category", "description": "Description", "products": None}])


def test_create_objects_rejects_non_object_product() -> None:
    data = [{"name": "Category", "description": "Description", "products": ["product"]}]

    with pytest.raises(ValueError, match="product"):
        create_objects_from_json(data)
