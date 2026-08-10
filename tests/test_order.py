from __future__ import annotations

import pytest

from src.base_entity import BaseEntity
from src.category import Category
from src.order import Order
from src.product import Product


def test_base_entity_is_abstract() -> None:
    with pytest.raises(TypeError):
        BaseEntity()  # type: ignore[abstract]


def test_category_and_order_share_base_entity() -> None:
    assert issubclass(Category, BaseEntity)
    assert issubclass(Order, BaseEntity)


def test_order_initialization(smartphone: Product) -> None:
    order = Order(smartphone, 2)

    assert order.product is smartphone
    assert order.quantity == 2
    assert order.total_price == 360000.0
    assert order.total_quantity == 2
    assert order.total_cost == 360000.0
    assert str(order) == "Заказ: Samsung Galaxy S23 Ultra, количество: 2 шт., стоимость: 360000.0 руб."


@pytest.mark.parametrize("quantity", [0, -1])
def test_order_rejects_non_positive_quantity(smartphone: Product, quantity: int) -> None:
    with pytest.raises(ValueError, match="positive"):
        Order(smartphone, quantity)


def test_order_rejects_non_product() -> None:
    with pytest.raises(TypeError, match="Product"):
        Order("Not a product", 1)  # type: ignore[arg-type]
