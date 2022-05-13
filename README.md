Разработать проект «Книга рецептов» в виде веб-сайта, используя фреймворк Django 3.

В панели управления (/admin) пользователь должен иметь возможность ввести:
1. список ингредиентов для рецепта;
2. добавить текст и название рецепта.
В публичной части сайта пользователь должен иметь возможность просмотра введенных рецептов с выводом ингредиентов с возможностью фильтрации по ингредиентам и названию рецепта. Нужно учесть, что один ингредиент может встречаться в нескольких рецептах.
Для дизайна веб-сайта можно использовать стандартные шаблоны Bootstrap.
Необходимо разработать схему базы данных, описав соответствующие модели для таблиц. Таким образом, схема базы данных должна быть приведена к третьей нормальной форме (3НФ).
При первом запуске проекта база данных должна наполниться данными благодаря миграции и добавлению фикстур.
Проект должен быть упакован в Docker (иметь Dockerfile и docker-compose.yml).
Необходимо опубликовать проект на GitHub и оформить Readme.md с описанием и инструкцией по запуску.




Инструкция по запуску:

2. Создание контейнеров через команду: 
 - docker-compose -f docker-compose.yml up --build 
2. Создание и инициализация БД:
 - docker cp ./entrypoint.sql postgres:/entrypoint.sql 
 - docker exec -u postgres postgres psql postgres postgres -f /entrypoint.sql
4. Перезапускаем контейнеры:
 - docker-compose -f docker-compose.yml up --build
5. Заполняем БД:
 - docker exec book python manage.py loaddata data

