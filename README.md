# API_QUIZ
## Описание
API проект создания опросов.
Каждый объет опроса (Quiz) содержит в себе вопросы (Question)
и варианты ответов на них (Choice).
Ответы пользователя хранятся в объекте Answers.
## Установка

Создать и активировать виртуальное окружение:

```sh
python3 -m venv venv
source venv/bin/activate
```
Установить зависимости из файла requirements.txt:
```sh
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
Выполнить миграции:


```sh
python3 manage.py migrate
python3 manage.py runserver
```

## Запросы API
Получить полный список опросов (с пагинацией):
```sh
http://127.0.0.1:8000/api/quiz/
```
Для авторизации администратора в системе нужно передать
username и password в api по адресу:
```sh
http://127.0.0.1:8000/api/api-token-auth/
```
Будет получен токен, который нужно передавать вместе с 
POST/PATCH/PUT/DELETE запросами.

Более подробная информация досупна в документации API:
```sh
http://127.0.0.1:8000/swagger/
```
Telegram: @shchegolyaev 