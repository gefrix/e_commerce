from __future__ import annotations

from unittest.mock import patch

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


def test_price_is_private(smartphone: Product) -> None:
    assert not hasattr(smartphone, "__price")
    assert smartphone._Product__price == 180000.0


def test_new_product_creates_product_from_dictionary() -> None:
    product = Product.new_product(
        {
            "name": "New product",
            "description": "Description",
            "price": 1500.5,
            "quantity": 10,
        }
    )

    assert isinstance(product, Product)
    assert product.name == "New product"
    assert product.description == "Description"
    assert product.price == 1500.5
    assert product.quantity == 10


def test_new_product_merges_duplicate_and_keeps_higher_existing_price() -> None:
    existing = Product("Phone", "Old description", 2000.0, 3)

    result = Product.new_product(
        {
            "name": "Phone",
            "description": "New description",
            "price": 1500.0,
            "quantity": 4,
        },
        [existing],
    )

    assert result is existing
    assert existing.quantity == 7
    assert existing.price == 2000.0


def test_new_product_merges_duplicate_and_uses_higher_new_price() -> None:
    existing = Product("Phone", "Description", 2000.0, 3)

    result = Product.new_product(
        {
            "name": "Phone",
            "description": "Description",
            "price": 2500.0,
            "quantity": 4,
        },
        [existing],
    )

    assert result is existing
    assert existing.quantity == 7
    assert existing.price == 2500.0


def test_new_product_creates_new_item_when_duplicate_is_absent() -> None:
    existing = Product("Phone", "Description", 2000.0, 3)

    result = Product.new_product(
        {
            "name": "Television",
            "description": "Description",
            "price": 5000.0,
            "quantity": 1,
        },
        [existing],
    )

    assert result is not existing
    assert result.name == "Television"


def test_price_setter_increases_price_without_confirmation(smartphone: Product) -> None:
    with patch("builtins.input") as input_mock:
        smartphone.price = 200000.0

    assert smartphone.price == 200000.0
    input_mock.assert_not_called()


def test_price_setter_accepts_confirmed_decrease(smartphone: Product) -> None:
    with patch("builtins.input", return_value="Y") as input_mock:
        smartphone.price = 150000.0

    assert smartphone.price == 150000.0
    input_mock.assert_called_once()


def test_price_setter_rejects_unconfirmed_decrease(smartphone: Product) -> None:
    with patch("builtins.input", return_value="n"):
        smartphone.price = 150000.0

    assert smartphone.price == 180000.0


def test_price_setter_rejects_non_positive_values(
    smartphone: Product,
    capsys: object,
) -> None:
    smartphone.price = -100.0
    smartphone.price = 0.0

    output = capsys.readouterr().out  # type: ignore[attr-defined]
    assert output == (
        "Цена не должна быть нулевая или отрицательная\n" "Цена не должна быть нулевая или отрицательная\n"
    )
    assert smartphone.price == 180000.0
