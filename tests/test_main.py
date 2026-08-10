from __future__ import annotations

from main import main
from src.category import Category


def test_main_runs_assignment_scenario(capsys: object) -> None:
    main()

    output = capsys.readouterr().out  # type: ignore[attr-defined]
    assert "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт." in output
    assert "Смартфоны, количество продуктов: 27 шт." in output
    assert "2580000.0" in output
    assert "1334000.0" in output
    assert "2114000.0" in output
    assert Category.category_count == 1
    assert Category.product_count == 3
