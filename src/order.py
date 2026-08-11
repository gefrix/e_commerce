from __future__ import annotations

from src.base_entity import BaseEntity
from src.product import Product


class Order(BaseEntity):
    """A purchase order containing exactly one product type."""

    def __init__(self, product: Product, quantity: int) -> None:
        if not isinstance(product, Product):
            raise TypeError("An order can contain only a Product object")
        if quantity <= 0:
            raise ValueError("Order quantity must be positive")

        self.product = product
        self.quantity = int(quantity)
        self.total_price = product.price * self.quantity

    @property
    def total_quantity(self) -> int:
        return self.quantity

    @property
    def total_cost(self) -> float:
        return self.total_price

    def __str__(self) -> str:
        return f"Заказ: {self.product.name}, количество: {self.quantity} шт., стоимость: {self.total_price} руб."
