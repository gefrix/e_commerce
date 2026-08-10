from __future__ import annotations

from src.product import Product


class Smartphone(Product):
    """A smartphone product with device-specific characteristics."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = float(efficiency)
        self.model = model
        self.memory = int(memory)
        self.color = color
