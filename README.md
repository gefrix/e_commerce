# E-commerce

Учебное ядро интернет-магазина, реализованное с применением объектно-ориентированного подхода.
Проект последовательно развивается в домашних заданиях SkyPro «14.1 Введение в ООП», «14.2 Режимы доступа»
и «15.1 Магические методы».

## Реализованная функциональность

- класс `Product` с атрибутами названия, описания, цены и количества на складе;
- класс `Category` с названием, описанием и коллекцией объектов `Product`;
- автоматический подсчёт созданных категорий через `Category.category_count`;
- автоматический подсчёт товаров в категориях через `Category.product_count`;
- приватное хранение списка товаров категории;
- добавление товара через `Category.add_product()`;
- строковый геттер `Category.products` со сведениями о цене и остатке;
- фабричный класс-метод `Product.new_product()`;
- объединение количества и выбор большей цены при создании дубликата товара;
- приватное хранение цены и управление ею через `Product.price`;
- защита от нулевой и отрицательной цены;
- подтверждение снижения цены пользователем;
- строковое представление товара через `Product.__str__()`;
- строковое представление категории с суммарным количеством товаров на складе;
- сложение полной стоимости складских остатков двух товаров через `Product.__add__()`;
- перебор товаров категории с помощью `CategoryIterator`;
- чтение исходных данных из JSON;
- преобразование JSON-данных в объекты `Category` и `Product`;
- демонстрационный сценарий из приложенного к заданию файла `main.py`;
- тесты и отчёт о покрытии функционального кода.

Дополнительные задания с загрузкой данных из `products.json`, объединением дубликатов, подтверждением снижения цены
и итератором товаров категории также выполнены.

## Структура проекта

```text
e_commerce/
├── data/
│   └── products.json
├── src/
│   ├── category.py
│   ├── category_iterator.py
│   ├── product.py
│   └── utils.py
├── tests/
│   ├── conftest.py
│   ├── test_category.py
│   ├── test_category_iterator.py
│   ├── test_main.py
│   ├── test_product.py
│   └── test_utils.py
├── coverage_report.md
├── main.py
├── poetry.lock
└── pyproject.toml
```

## Установка

Для работы требуется Python 3.12 или новее и Poetry 2.x.

```bash
poetry install
```

Poetry создаст виртуальное окружение и установит инструменты разработки.

## Запуск

Запуск демонстрационного сценария:

```bash
poetry run python main.py
```

При попытке снизить цену сценарий запросит подтверждение: `y` применяет новую цену, любой другой ответ отменяет
изменение.

Загрузка категорий и товаров из JSON:

```python
from src.utils import load_categories_from_json

categories = load_categories_from_json("data/products.json")

print(categories[0].name)
print(categories[0].products)
```

Также доступны отдельные этапы загрузки:

```python
from src.utils import create_objects_from_json, read_json

raw_data = read_json("data/products.json")
categories = create_objects_from_json(raw_data)
```

## Проверка качества

Все тесты вместе с измерением покрытия:

```bash
poetry run pytest
```

Остальные проверки:

```bash
poetry run black --check src tests main.py
poetry run isort --check-only src tests main.py
poetry run flake8 src tests main.py
poetry run mypy src main.py
poetry check
```

Фактическое покрытие функционального кода составляет **99%**. Подробный результат сохранён в
[`coverage_report.md`](coverage_report.md).

## GitFlow

- `main` — стабильная версия проекта;
- `develop` — ветка интеграции;
- `feature/homework-14-1` — выполненное задание 14.1;
- `feature/homework-14-2` — выполненное задание 14.2;
- `feature/homework-15-1` — полностью выполненное задание 15.1.

Для сдачи работы нужно создать Pull Request из `feature/homework-15-1` в `develop`.

