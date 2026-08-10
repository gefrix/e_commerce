from __future__ import annotations

from unittest.mock import patch

from main import main
from src.category import Category


def test_main_runs_assignment_scenario(capsys: object) -> None:
    with patch("builtins.input", return_value="y"):
        main()

    output = capsys.readouterr().out  # type: ignore[attr-defined]
    assert "Samsung Galaxy S23 Ultra" in output
    assert '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.' in output
    assert "Цена не должна быть нулевая или отрицательная" in output
    assert Category.category_count == 1
    assert Category.product_count == 4
