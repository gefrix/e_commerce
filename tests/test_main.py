from __future__ import annotations

from main import main
from src.category import Category


def test_main_runs_assignment_scenario(capsys: object) -> None:
    main()

    output = capsys.readouterr().out  # type: ignore[attr-defined]
    assert "Product('Samsung Galaxy S23 Ultra'" in output
    assert "Samsung Galaxy S23 Ultra" in output
    assert "Смартфоны, как средство" in output
    assert "Телевизоры" in output
    assert "True" in output
    assert Category.category_count == 2
    assert Category.product_count == 4
