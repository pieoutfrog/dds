# Django Transaction Management API

Это проект Django REST Framework, который предоставляет API для управления транзакциями, категориями, подкатегориями и
типами транзакций. Он включает в себя функции для создания, чтения, обновления и удаления (CRUD) объектов этих моделей.

## Установка

### Требования

- Python 3.6+
- Django 5.1+
- Django REST Framework 3.15+

### Установка

### 1. Клонируйте репозиторий:

``git clone https://github.com/pieoutfrog/dds``

``cd dds``

### 2. Создайте и активируйте виртуальное окружение:

``python -m venv venv``

``source venv/bin/activate`` # Для macOS/Linux

``venv\Scripts\activate`` # Для Windows

### 3. Установите зависимости:

``pip install -r requirements.txt``

### 4. Настройте базу данных в файле `settings.py`.

Используйте SQLite, PostgreSQL или другую СУБД по вашему выбору.

### 5. Примените миграции:

``python manage.py migrate``

### 6. Создайте суперпользователя для доступа к админке:

``python manage.py createsuperuser``

### 7. Запустите сервер разработки:

``python manage.py runserver``

## Использование

### Эндпоинты API

- **Транзакции**
    - `GET /api/transactions/` - Получить список всех транзакций (поддерживает фильтрацию по параметрам: `status`,
      `type`, `category`, `subcategory`, `start_date`, `end_date`).
    - `POST /api/transactions/` - Создать новую транзакцию.
    - `GET /api/transactions/{id}/` - Получить информацию о транзакции по ID.
    - `PUT /api/transactions/{id}/` - Обновить информацию о транзакции.
    - `DELETE /api/transactions/{id}/` - Удалить транзакцию.

- **Категории**
    - `GET /api/categories/` - Получить список всех категорий.
    - `POST /api/categories/` - Создать новую категорию.
    - `GET /api/categories/{id}/` - Получить информацию о категории по ID.
    - `PUT /api/categories/{id}/` - Обновить информацию о категории.
    - `DELETE /api/categories/{id}/` - Удалить категорию.

- **Подкатегории**
    - `GET /api/subcategories/` - Получить список всех подкатегорий.
    - `POST /api/subcategories/` - Создать новую подкатегорию.
    - `GET /api/subcategories/{id}/` - Получить информацию о подкатегории по ID.
    - `PUT /api/subcategories/{id}/` - Обновить информацию о подкатегории.
    - `DELETE /api/subcategories/{id}/` - Удалить подкатегорию.

- **Типы**
    - `GET /api/types/` - Получить список всех типов.
    - `POST /api/types/` - Создать новый тип.
    - `GET /api/types/{id}/` - Получить информацию о типе по ID.
    - `PUT /api/types/{id}/` - Обновить информацию о типе.
    - `DELETE /api/types/{id}/` - Удалить тип.