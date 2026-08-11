from __future__ import annotations

from src.base_entity import BaseEntity
from src.exceptions import ZeroQuantityError
from src.product import Product


class Order(BaseEntity):
    """A purchase order containing exactly one product type."""

    def __init__(self, product: Product, quantity: int) -> None:
        if not isinstance(product, Product):
            raise TypeError("An order can contain only a Product object")

        normalized_quantity = int(quantity)
        try:
            if product.quantity == 0 or normalized_quantity == 0:
                raise ZeroQuantityError
            if normalized_quantity < 0:
                raise ValueError("Order quantity must be positive")
        except ZeroQuantityError as error:
            print(error)
            raise
        else:
            self.product = product
            self.quantity = normalized_quantity
            self.total_price = product.price * self.quantity
            print("Товар успешно добавлен")
        finally:
            print("Обработка добавления товара завершена")

    @property
    def total_quantity(self) -> int:
        return self.quantity

    @property
    def total_cost(self) -> float:
        return self.total_price

    def __str__(self) -> str:
        return f"Заказ: {self.product.name}, количество: {self.quantity} шт., стоимость: {self.total_price} руб."
