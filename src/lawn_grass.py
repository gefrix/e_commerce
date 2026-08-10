from __future__ import annotations

from src.product import Product


class LawnGrass(Product):
    """A lawn grass product with cultivation characteristics."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(
            name,
            description,
            price,
            quantity,
            country,
            germination_period,
            color,
        )
        self.country = country
        self.germination_period = germination_period
        self.color = color
