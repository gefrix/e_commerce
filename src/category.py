from __future__ import annotations

from collections.abc import Iterator

from src.base_entity import BaseEntity
from src.product import Product


class Category(BaseEntity):
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
        if not isinstance(product, Product):
            raise TypeError("Only Product objects and their subclasses can be added to a category")

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Return all products formatted for display."""
        return "".join(f"{product}\n" for product in self.__products)

    def __str__(self) -> str:
        """Return the category name and total stock quantity."""
        return f"{self.name}, количество продуктов: {self.total_quantity} шт."

    @property
    def total_quantity(self) -> int:
        """Return the total number of product units in the category."""
        return sum(product.quantity for product in self.__products)

    @property
    def total_cost(self) -> float:
        """Return the total stock value of all products in the category."""
        return sum(product.price * product.quantity for product in self.__products)

    def _iter_products(self) -> Iterator[Product]:
        """Return an internal iterator without exposing the private list."""
        return iter(self.__products)


class CategoryIterator:
    """Iterate over products stored in one category."""

    def __init__(self, category: Category) -> None:
        self._products = category._iter_products()

    def __iter__(self) -> CategoryIterator:
        return self

    def __next__(self) -> Product:
        return next(self._products)
