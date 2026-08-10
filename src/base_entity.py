from __future__ import annotations

from abc import ABC, abstractmethod


class BaseEntity(ABC):
    """Expose aggregate quantity and cost shared by categories and orders."""

    @property
    @abstractmethod
    def total_quantity(self) -> int:
        """Return the number of product units represented by the entity."""

    @property
    @abstractmethod
    def total_cost(self) -> float:
        """Return the total value represented by the entity."""
