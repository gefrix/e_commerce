# Отчёт о покрытии тестами

Дата проверки: 10 августа 2026 года.

Команда:

```bash
poetry run pytest --cov=src --cov=main --cov-report=term-missing
```

Результат:

```text
25 passed

Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
main.py              26      1    96%   53
src/__init__.py       3      0   100%
src/category.py      21      0   100%
src/product.py       40      0   100%
src/utils.py         31      0   100%
-----------------------------------------------
TOTAL               121      1    99%
```

Требуемое покрытие функционального кода — более 75%. Фактическое покрытие — **99%**.
