from __future__ import annotations

import pytest

from src.base_product import BaseProduct
from src.product import Product


def test_base_product_is_abstract() -> None:
    with pytest.raises(TypeError):
        BaseProduct()  # type: ignore[abstract]


def test_product_inherits_base_product() -> None:
    assert issubclass(Product, BaseProduct)
