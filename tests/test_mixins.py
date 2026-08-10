from __future__ import annotations

from src.base_product import BaseProduct
from src.mixin import CreationInfoMixin as ExportedCreationInfoMixin
from src.mixin import MixinLog as ExportedMixinLog
from src.mixins import CreationInfoMixin, MixinLog
from src.product import Product
from src.smartphone import Smartphone


def test_product_uses_multiple_inheritance() -> None:
    assert Product.__bases__ == (CreationInfoMixin, BaseProduct)
    assert issubclass(Product, CreationInfoMixin)
    assert issubclass(Product, BaseProduct)


def test_creation_mixin_prints_product_class_and_arguments(capsys: object) -> None:
    Product("Продукт1", "Описание продукта", 1200, 10)

    output = capsys.readouterr().out  # type: ignore[attr-defined]
    assert output == "Product('Продукт1', 'Описание продукта', 1200, 10)\n"


def test_creation_mixin_logs_all_subclass_arguments(capsys: object) -> None:
    Smartphone("Телефон", "Описание", 1000.0, 2, 95.5, "Model", 256, "Черный")

    output = capsys.readouterr().out  # type: ignore[attr-defined]
    assert output == "Smartphone('Телефон', 'Описание', 1000.0, 2, 95.5, 'Model', 256, 'Черный')\n"


def test_product_repr_matches_creation_information(capsys: object) -> None:
    product = Product("Продукт1", "Описание продукта", 1200, 10)
    capsys.readouterr()  # type: ignore[attr-defined]

    assert repr(product) == "Product('Продукт1', 'Описание продукта', 1200, 10)"


def test_mixin_compatibility_exports() -> None:
    assert MixinLog is CreationInfoMixin
    assert ExportedCreationInfoMixin is CreationInfoMixin
    assert ExportedMixinLog is CreationInfoMixin
