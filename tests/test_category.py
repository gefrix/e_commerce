from __future__ import annotations

from src.category import Category
from src.product import Product


def test_category_initialization(
    category: Category,
    products: list[Product],
) -> None:
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны для связи и повседневных задач"
    assert category.products == products


def test_category_count_increases_automatically(products: list[Product]) -> None:
    first = Category("Смартфоны", "Описание", products)
    second = Category("Телевизоры", "Описание", [])

    assert first.category_count == 2
    assert second.category_count == 2
    assert Category.category_count == 2


def test_product_count_uses_product_list_length(products: list[Product]) -> None:
    Category("Смартфоны", "Описание", products)
    Category(
        "Телевизоры",
        "Описание",
        [Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)],
    )

    assert Category.product_count == 4


def test_empty_category_does_not_increase_product_count() -> None:
    category = Category("Пустая категория", "Пока без товаров", [])

    assert category.category_count == 1
    assert category.product_count == 0
