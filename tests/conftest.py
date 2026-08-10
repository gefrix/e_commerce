from __future__ import annotations

from collections.abc import Generator

import pytest

from src.category import Category
from src.product import Product


@pytest.fixture(autouse=True)
def reset_category_counters() -> Generator[None, None, None]:
    """Keep class-level counter tests isolated from one another."""
    Category.category_count = 0
    Category.product_count = 0
    yield
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def smartphone() -> Product:
    """Return a representative product."""
    return Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
    )


@pytest.fixture
def products(smartphone: Product) -> list[Product]:
    """Return a small product collection."""
    return [
        smartphone,
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
    ]


@pytest.fixture
def category(products: list[Product]) -> Category:
    """Return a category containing the product collection."""
    return Category(
        "Смартфоны",
        "Смартфоны для связи и повседневных задач",
        products,
    )
