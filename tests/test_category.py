from __future__ import annotations

import pytest

from src.category import Category
from src.product import Product


def test_category_initialization(
    category: Category,
    products: list[Product],
) -> None:
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны для связи и повседневных задач"
    assert category.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_product_collection_is_private(category: Category) -> None:
    assert not hasattr(category, "__products")
    assert isinstance(category._Category__products, list)


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
    assert category.products == ""


def test_add_product_appends_product_and_updates_counter(category: Category) -> None:
    television = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

    result = category.add_product(television)

    assert result is None
    assert Category.product_count == 4
    assert category.products.endswith('55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n')


def test_category_string_contains_total_stock_quantity(category: Category) -> None:
    assert str(category) == "Смартфоны, количество продуктов: 27 шт."


def test_empty_category_string_contains_zero_quantity() -> None:
    category = Category("Пустая категория", "Без товаров", [])

    assert str(category) == "Пустая категория, количество продуктов: 0 шт."


def test_add_product_rejects_non_product(category: Category) -> None:
    initial_count = Category.product_count

    with pytest.raises(TypeError, match="Product objects"):
        category.add_product("Not a product")  # type: ignore[arg-type]

    assert Category.product_count == initial_count
