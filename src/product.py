from __future__ import annotations

from typing import Any, cast


class Product:
    """A product available in the online store."""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ) -> None:
        """Initialize a product with its descriptive and stock data."""
        self.name = name
        self.description = description
        self.__price = float(price)
        self.quantity = int(quantity)

    @classmethod
    def new_product(
        cls,
        product: dict[str, Any],
        products: list[Product] | None = None,
    ) -> Product:
        """Create a product or merge it with an existing product of the same name."""
        name = str(product["name"])
        description = str(product["description"])
        price = float(product["price"])
        quantity = int(product["quantity"])

        if products is not None:
            for existing_product in products:
                if existing_product.name == name:
                    existing_product.quantity += quantity
                    if price > existing_product.price:
                        existing_product.price = price
                    return existing_product

        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        """Return the product price."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Validate and, when needed, confirm a new product price."""
        normalized_price = float(new_price)
        if normalized_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if normalized_price < self.__price:
            answer = input("Цена снижается. Подтвердите изменение (y/n): ")
            if answer.strip().casefold() != "y":
                return

        self.__price = normalized_price

    def __str__(self) -> str:
        """Return product details in the store display format."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: object) -> float:
        """Return the total stock value of two products."""
        if type(self) is not type(other):
            raise TypeError("Products can only be added to other products of the same type")

        other_product = cast(Product, other)
        return self.price * self.quantity + other_product.price * other_product.quantity
