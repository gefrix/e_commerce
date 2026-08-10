from __future__ import annotations

from src.product import Product


def test_product_initialization(smartphone: Product) -> None:
    assert smartphone.name == "Samsung Galaxy S23 Ultra"
    assert smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone.price == 180000.0
    assert smartphone.quantity == 5


def test_product_uses_numeric_attribute_types() -> None:
    product = Product("Test", "Description", 100, 2.0)  # type: ignore[arg-type]

    assert isinstance(product.price, float)
    assert isinstance(product.quantity, int)
