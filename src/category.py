from __future__ import annotations

from src.product import Product


class Category:
    """A product category with counters shared by all category objects."""

    category_count: int = 0
    product_count: int = 0

    name: str
    description: str
    products: list[Product]

    def __init__(
        self,
        name: str,
        description: str,
        products: list[Product],
    ) -> None:
        """Initialize a category and update the shared counters."""
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)
