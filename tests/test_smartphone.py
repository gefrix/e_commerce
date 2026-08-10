from __future__ import annotations

import pytest

from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def smartphone() -> Smartphone:
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )


def test_smartphone_inherits_product(smartphone: Smartphone) -> None:
    assert isinstance(smartphone, Product)
    assert issubclass(Smartphone, Product)
    assert Smartphone.__bases__ == (Product,)


def test_smartphone_initialization(smartphone: Smartphone) -> None:
    assert smartphone.name == "Samsung Galaxy S23 Ultra"
    assert smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone.price == 180000.0
    assert smartphone.quantity == 5
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "S23 Ultra"
    assert smartphone.memory == 256
    assert smartphone.color == "Серый"


def test_smartphone_inherits_string_representation(smartphone: Smartphone) -> None:
    assert str(smartphone) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_smartphones_of_same_class_can_be_added(smartphone: Smartphone) -> None:
    second = Smartphone("Iphone 15", "512GB", 210000.0, 8, 98.2, "15", 512, "Gray space")

    assert smartphone + second == 2580000.0


def test_smartphone_cannot_be_added_to_other_product_class(smartphone: Smartphone) -> None:
    grass = LawnGrass("Газонная трава", "Описание", 500.0, 20, "Россия", "7 дней", "Зеленый")

    with pytest.raises(TypeError):
        _ = smartphone + grass

    with pytest.raises(TypeError):
        _ = smartphone + Product("Обычный товар", "Описание", 100.0, 1)
