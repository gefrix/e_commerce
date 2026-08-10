from __future__ import annotations

import pytest

from src.lawn_grass import LawnGrass
from src.product import Product


@pytest.fixture
def lawn_grass() -> LawnGrass:
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )


def test_lawn_grass_inherits_product(lawn_grass: LawnGrass) -> None:
    assert isinstance(lawn_grass, Product)
    assert issubclass(LawnGrass, Product)


def test_lawn_grass_initialization(lawn_grass: LawnGrass) -> None:
    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.description == "Элитная трава для газона"
    assert lawn_grass.price == 500.0
    assert lawn_grass.quantity == 20
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == "7 дней"
    assert lawn_grass.color == "Зеленый"


def test_lawn_grass_inherits_string_representation(lawn_grass: LawnGrass) -> None:
    assert str(lawn_grass) == "Газонная трава, 500.0 руб. Остаток: 20 шт."


def test_lawn_grass_objects_can_be_added(lawn_grass: LawnGrass) -> None:
    second = LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )

    assert lawn_grass + second == 16750.0
