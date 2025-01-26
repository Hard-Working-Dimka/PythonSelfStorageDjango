# PythonSelfStorageDjango

**PythonSelfStorageDjango** — это веб-приложение на основе Django, предназначенное для управления арендой ячеек складов.

## Особенноти

- **Управление складами**: создание, редактирование информации о складах.
- **Управление заказами**: создание/сортировка по параметрам/
- **Управление ячейками**: создание пустых ячеек на складе, указание размера

## Требования

- Django==5.1.1
- environs==14.1.0
- djangorestframework==3.15.2

## Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/GoNt1eRRR/PythonSelfStorageDjango
cd PythonSelfStorageDjango
```
2. Создайте виртуальное окружение:

```bash
python3 -m venv env
source venv/bin/activate  # Для Windows: venv\Scripts\activate
```

Установите зависимости:

```
pip install -r requirements.txt
```
Примените миграции базы данных:
```
python manage.py migrate
```

Создайте суперпользователя для доступа к административной панели:
```
python manage.py createsuperuser
```
Запустите сервер разработки:
```
python manage.py runserver
```

## Структура проекта:

* self_storage/ — основной модуль проекта.
* api/ — модуль, содержащий реализацию API.
* storage/ — модуль, отвечающий админ-панель, также определения моделей
* manage.py — скрипт для управления проектом.
* requirements.txt — файл с перечнем зависимостей проекта.

## API
### Сustom-user
- `GET /api/custom-user/`: Получить список всех пользователей
- `POST /api/custom-user/`: Создать нового пользователя
- `GET /api/custom-user/{id}/`: Получить данные пользователя по ID
- `PATCH /api/custom-user/{id}/`: Обновить данные пользователя
- `DELETE /api/custom-user/{id}/`: Удалить пользователя

### Storage
- `GET /api/storage/`: Получить список всех складах
- `POST /api/storage/`: Создать новый склад
- `GET /api/storage/{id}/`: Получить информацию о складе по ID
- `PATCH /api/storage/{id}/`: Обновить данные склада
- `DELETE /api/storage/{id}/`: Удалить склад

### Storage-unit
- `GET /api/storage-unit/`: Получить список всех ячеек
- `POST /api/storage-unit/`: Добавить новую ячейку
- `GET /api/storage-unit/{id}/`: Получить информацию о ячейке по ID
- `PATCH /api/storage-unit/{id}/`: Обновить данные ячейки
- `DELETE /api/storage-unit/{id}/`: Удалить ячейку

### Order
- `GET /api/order/`: Получить список всех заказов
- `POST /api/order/`: Добавить новый заказ
- `GET /api/order/{id}/`: Получить информацию о заказе по ID
- `PATCH /api/order/{id}/`: Обновить данные заказа
- `DELETE /api/order/{id}/`: Удалить заказ


## Модели

### custom-user
Расширенная версия `AbstractUser` с дополнительными полями:
- **Поля**: `telegram_id `, `telegram_name `.

---

### Storage
Представляет склад.
- **Поля**: `name `, `location `,  `max_capacity `.

---

### StorageUnit
Представляет ячейку, которая связана со складом.
- **Связь по внешнему ключу с:** `storage` из модели `Storage`.
- **Поля**: `storage `, `unit_number `, `size `, `is_occupied `.

---

### Order
Представляет заказ.
- **Связь по внешнему ключу с:** `customer` из модели `CustomUser`, `storage_unit` из модели `StorageUnit`, `storage` из модели `Storage`.
- **Поля**: `address `, `phone_number `, `full_name `, `start_date `, `end_date `, `status `, `qr_issued `, `qr_code `.


## Админ-панель
Панель администратора доступна по адресу /admin/ для управления всеми моделями
