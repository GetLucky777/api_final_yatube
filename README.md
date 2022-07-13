# Описание

Это проект API для соц. сети дневников Yatube. Вы можете работать с постами (есть поддержка пагинации), комментариями, группами и подписками (есть поддержка поиска по подпискам). Документация доступна по адресу http://127.0.0.1:8000/redoc/

# Используемые технологии

- Django 2.2.16
- Django REST Framework 3.12.4
- Simple JWT 4.7.2

# Установка

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/kittygram.git
```

```
cd kittygram
```

Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:
```
python3 manage.py migrate
```

Запустить проект:
```
python3 manage.py runserver
```

# Примеры запросов

GET /api/v1/posts/
Ответ:
```
[
{
"id": 1,
"text": "GetLucky's text redacted 2",
"pub_date": "2022-04-11T15:15:36.222383Z",
"author": "GetLucky",
"image": null,
"group": 2
},
{
"id": 3,
"text": "My fav text",
"pub_date": "2022-04-11T15:21:10.562804Z",
"author": "GetLucky",
"image": null,
"group": 2
},
{
"id": 4,
"text": "Comment 1",
"pub_date": "2022-04-11T15:23:13.223591Z",
"author": "FuturaFree",
"image": null,
"group": 2
},
{
"id": 5,
"text": "Second futuras post",
"pub_date": "2022-04-11T15:40:15.312407Z",
"author": "FuturaFree",
"image": null,
"group": null
}
]
```

GET api/v1/posts/{post_id}/comments/{id}/
Ответ:
```
{
"id": 1,
"author": "FuturaFree",
"post": 1,
"text": "Ffdgljkljkljkldfg",
"created": "2022-04-11T15:24:40.839243Z"
}
```

