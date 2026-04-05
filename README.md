# Stellar Burgers — Автотесты на Selenium

Проект содержит автоматизированные UI-тесты для сайта [Stellar Burgers](https://stellarburgers.education-services.ru/).

## Структура проекта

```
stellar_burgers/
├── locators/
│   ├── __init__.py
│   └── locators.py        # Локаторы всех элементов страниц
├── tests/
│   ├── conftest.py        # Фикстуры pytest
│   ├── test_registration.py    # Тесты регистрации
│   ├── test_login.py           # Тесты входа
│   ├── test_personal_account.py # Тесты личного кабинета и выхода
│   └── test_constructor.py     # Тесты конструктора
├── helpers.py             # Генераторы данных и константы URL
├── requirements.txt
├── .gitignore
└── README.md
```

## Покрытие тестами

| Функциональность | Тесты |
|---|---|
| Регистрация | Успешная регистрация, ошибка при коротком пароле |
| Вход | Через кнопку на главной, через «Личный кабинет», через страницу регистрации, через страницу восстановления пароля |
| Личный кабинет | Переход в кабинет |
| Навигация из кабинета | Переход в конструктор через ссылку и логотип |
| Выход | Выход по кнопке «Выйти» |
| Конструктор | Переходы к разделам «Булки», «Соусы», «Начинки» |

## Требования

- Python 3.8+
- Google Chrome (последняя версия)
- ChromeDriver (версия должна совпадать с версией Chrome)

## Установка

```bash
# Клонировать репозиторий
git clone <repo-url>
cd stellar_burgers

# Установить зависимости
pip install -r requirements.txt
```

## Запуск тестов

```bash
# Все тесты
pytest tests/

# Конкретный файл
pytest tests/test_registration.py

# С подробным выводом
pytest tests/ -v

# Запуск в headless-режиме (без открытия браузера)
# Раскомментируй строку с --headless в conftest.py
```

## Генерация тестовых данных

- `generate_email()` — генерирует уникальный email формата `test_testov_999_XXX@yandex.ru`
- `generate_password()` — генерирует случайный пароль длиной 8 символов
