# Отчёт о покрытии тестами

Дата проверки: 10 августа 2026 года.

Команда:

```bash
poetry run pytest --cov=src --cov=main --cov-report=term-missing
```

Результат:

```text
44 passed

Name                       Stmts   Miss  Cover   Missing
--------------------------------------------------------
main.py                       48      3    94%   90, 114, 118
src/__init__.py                5      0   100%
src/category.py               36      0   100%
src/category_iterator.py       2      0   100%
src/lawn_grass.py              8      0   100%
src/product.py                47      0   100%
src/smartphone.py              9      0   100%
src/utils.py                  31      0   100%
--------------------------------------------------------
TOTAL                        186      3    98%
```

Требуемое покрытие функционального кода — более 75%. Фактическое покрытие — **98%**.
