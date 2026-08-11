# Отчёт о покрытии тестами

Дата проверки: 10 августа 2026 года.

Команда:

```bash
poetry run pytest --cov=src --cov=main --cov-report=term-missing
```

Результат:

```text
57 passed

Name                       Stmts   Miss  Cover   Missing
--------------------------------------------------------
main.py                       28      1    96%   53
src/__init__.py                9      0   100%
src/base_entity.py             9      0   100%
src/base_product.py            9      0   100%
src/category.py               42      0   100%
src/category_iterator.py       2      0   100%
src/lawn_grass.py              8      0   100%
src/mixin.py                   2      0   100%
src/mixins.py                 13      0   100%
src/order.py                  20      0   100%
src/product.py                50      0   100%
src/smartphone.py              9      0   100%
src/utils.py                  31      0   100%
--------------------------------------------------------
TOTAL                        232      1    99%
```

Требуемое покрытие функционального кода — более 75%. Фактическое покрытие — **99%**.
