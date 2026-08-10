from __future__ import annotations

from main import main
from src.category import Category


def test_main_runs_assignment_scenario(capsys: object) -> None:
    main()

    output = capsys.readouterr().out  # type: ignore[attr-defined]
    assert "Samsung Galaxy S23 Ultra" in output
    assert "S23 Ultra" in output
    assert "Газонная трава" in output
    assert "2580000.0" in output
    assert "16750.0" in output
    assert "Возникла ошибка TypeError при попытке сложения" in output
    assert "Возникла ошибка TypeError при добавлении не продукта" in output
    assert Category.category_count == 2
    assert Category.product_count == 5
