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


def test_order_rejects_zero_quantity(smartphone: Product, capsys: object) -> None:
    capsys.readouterr()  # type: ignore[attr-defined]

    with pytest.raises(ValueError, match="^Товар с нулевым количеством не может быть добавлен$"):
        Order(smartphone, 0)

    output = capsys.readouterr().out  # type: ignore[attr-defined]
    assert output == ("Товар с нулевым количеством не может быть добавлен\n" "Обработка добавления товара завершена\n")


def test_order_rejects_negative_quantity(smartphone: Product) -> None:
    with pytest.raises(ValueError, match="positive"):
        Order(smartphone, -1)


def test_order_rejects_non_product() -> None:
    with pytest.raises(TypeError, match="Product"):
        Order("Not a product", 1)  # type: ignore[arg-type]
