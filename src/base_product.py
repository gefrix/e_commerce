from __future__ import annotations

from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Define the common interface required for every product type."""

    @abstractmethod
    def __init__(self) -> None:
        """Initialize a concrete product."""

    @abstractmethod
    def __str__(self) -> str:
        """Return a user-facing product description."""

    @abstractmethod
    def __add__(self, other: object) -> float:
        """Return the combined stock value of compatible products."""
