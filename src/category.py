from __future__ import annotations

from src.product import Product


class Category:
    """A product category with counters shared by all category objects."""

    category_count: int = 0
    product_count: int = 0

    name: str
    description: str
    __products: list[Product]

    def __init__(
        self,
        name: str,
        description: str,
        products: list[Product],
    ) -> None:
        """Initialize a category and update the shared counters."""
        self.name = name
        self.description = description
        self.__products = []

        Category.category_count += 1
        for product in products:
            self.add_product(product)

    def add_product(self, product: Product) -> None:
        """Add a product to the private collection and update the counter."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Return all products formatted for display."""
        return "".join(
            f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n" for product in self.__products
        )
