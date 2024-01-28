# Test_task_Simple_solutions
Тестовое - [клац](https://docs.google.com/document/d/1X8yV7jAZWZWhy3NG3m_Yi8lW4Bfa6ZNGDx95pHkE_qc/edit#heading=h.qn8kbnfz56hc)

### Запуск проекта
- Скачать и установить [Docker](https://docs.docker.com/get-docker/)
- Клонировать репозиторий ```git clone https://github.com/Pash1et/Test_task_Simple_solutions.git```
- В корне директории Test_task_Simple_solutions создать файл .env и заполнить его по примеру .env.example
- Выполнить команду ```docker compose up -d --build```
- Выполнить команду ```docker exec -it backend python manage.py migrate```
- Выполнить команду ```docker exec -it backend python manage.py collectstatic```
- Выполнить команду ```docker exec -it backend python manage.py createsuperuser```
- Перейти по адресу ```http://localhost/admin```

### Доступные эндпоинты
```GET /item_detail/{item_id}``` - Информаиця о товаре  
```GET /order_detail/{order_id}``` - Информация о корзине товаров  
```GET /item_buy/{item_id}``` - Получение session_id для товара  
```GET /order_buy/{order_id}``` - Получение session_id для коризны товаров 
