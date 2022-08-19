## Requirements

1. python = "^3.9"
2. fastapi = "^0.79.0"
3. uvicorn = "^0.18.2"
4. pydantic = "^1.9.2"
5. alembic = "^1.8.1"
6. SQLAlchemy = "^1.4.40"
7. psycopg2 = "^2.9.3"
8. pandas = "^1.4.3"

## Install

1. Install dependencies `poetry install`
2. Initialize pre-commit hooks `pre-commit install`
3. Start Postgres docker-container `docker-compose up -d`

## Alembic
Run migration with existing versions `poetry run alembic upgrade head`

## Environmental variable

| Title             | Default | Description                      | necessary |
| ----------------- | ------- | -------------------------------- | --------- |
| POSTGRES_DB       |         | Postgres URL                     | yes       |
| POSTGRES_USER     |         | Postgres User                    | yes       |
| POSTGRES_PASSWORD |         | Postgres Password                | yes       |

## Run application

1. Run command `uvicorn main:app --reload`

## Connect to database

1. `docker-compose exec postgres psql -U user -d ocm`


## Тестовое задание.

### Имеется файл с входными данными в формате csv

### Задача:
- подключить к проекту базу данных
- из имеющегося файла импортировать в базу данных **просроченные задачи**
- все даты из файла должны храниться в базе данных в полях типа datetime
- поле филиал из файла при записи в базу сократить до названия города
- реализовать API для получения записей, относящихся к определённому филиалу (городу), в формате **json**

### Стек:
- Язык программирования Python
- СУБД SQLite или PostgreSQL
- любые фреймворки и библиотеки на своё усмотрение

### Результат:
- оформить PR из форка
