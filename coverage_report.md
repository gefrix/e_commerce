# Отчёт о покрытии тестами

Дата проверки: 11 августа 2026 года.

Команда:

```bash
poetry run pytest --cov=src --cov=main --cov-report=term-missing
```

Результат:

```text
63 passed

Name                       Stmts   Miss  Cover   Missing
--------------------------------------------------------
main.py                       18      2    89%   17, 44
src/__init__.py               10      0   100%
src/base_entity.py             9      0   100%
src/base_product.py            9      0   100%
src/category.py               55      0   100%
src/category_iterator.py       2      0   100%
src/exceptions.py              5      0   100%
src/lawn_grass.py              8      0   100%
src/mixin.py                   2      0   100%
src/mixins.py                 13      0   100%
src/order.py                  30      0   100%
src/product.py                54      0   100%
src/smartphone.py              9      0   100%
src/utils.py                  31      0   100%
--------------------------------------------------------
TOTAL                        255      2    99%
```

Требуемое покрытие функционального кода — более 75%. Фактическое покрытие — **99%**.
