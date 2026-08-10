from __future__ import annotations

import pytest

from src.category import Category, CategoryIterator
from src.category_iterator import CategoryIterator as ExportedCategoryIterator
from src.product import Product


def test_category_iterator_returns_products_in_original_order(
    category: Category,
    products: list[Product],
) -> None:
    iterator = CategoryIterator(category)

    assert iter(iterator) is iterator
    assert list(iterator) == products


def test_category_iterator_raises_stop_iteration_after_last_product(
    category: Category,
    products: list[Product],
) -> None:
    iterator = CategoryIterator(category)

    assert next(iterator) is products[0]
    assert next(iterator) is products[1]
    assert next(iterator) is products[2]
    with pytest.raises(StopIteration):
        next(iterator)


def test_category_iterator_handles_empty_category() -> None:
    category = Category("Пустая категория", "Без товаров", [])

    assert list(CategoryIterator(category)) == []


def test_category_iterator_is_exported_from_helper_module() -> None:
    assert ExportedCategoryIterator is CategoryIterator
