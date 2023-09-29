# Simple API 

## Описание:

Простое Rest API для управления списком пользователей.

## Документация API

Статическая:

http://127.0.0.1:8000/api/schema/

Динамическая:

http://127.0.0.1:8000/api/schema/swagger/


## Технологии

Python 3.11

Django 4.2.5

Django REST Framework 3.14.0

DRF-Spectacular 0.26.4

PostgreSQL 15


## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone <HTTPS or SSH>
```

```
cd test_task_simple_api
```

Cоздать и активировать виртуальное окружение:
```
py -3.11 -m venv venv (Windows)
python3 -m venv venv (Linux, MacOS)

source venv/Scripts/activate (Windows)
source venv/bin/activate (Linux, MacOS)
```

Установить зависимости из файла requirements.txt:

```
cd backend
```

```
pip3 install -r requirements.txt
```

Скопировать файл .env_sample и переименовать в .env.

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

## Автор

[iliya12321](https://github.com/iliya12321)
