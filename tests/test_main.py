from __future__ import annotations

from main import main
from src.category import Category


def test_main_runs_assignment_scenario(capsys: object) -> None:
    main()

    output = capsys.readouterr().out  # type: ignore[attr-defined]
    assert "Возникла ошибка ValueError" in output
    assert "Product('Samsung Galaxy S23 Ultra'" in output
    assert "Товар успешно добавлен" in output
    assert "140333.33333333334" in output
    assert output.endswith("0.0\n")
    assert Category.category_count == 2
    assert Category.product_count == 3
