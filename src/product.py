from __future__ import annotations


class Product:
    """A product available in the online store."""

    name: str
    description: str
    price: float
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
        self.price = float(price)
        self.quantity = int(quantity)
