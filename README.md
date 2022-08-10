# plough
backend for little plough


## Start PostgreSQL
```
    export POSTGRES_DB=rwdb POSTGRES_PORT=5432 POSTGRES_USER=postgres POSTGRES_PASSWORD=postgres
    docker run --name pgdb --rm -e POSTGRES_USER="$POSTGRES_USER" -e POSTGRES_PASSWORD="$POSTGRES_PASSWORD" -e POSTGRES_DB="$POSTGRES_DB" postgres
```

## Run in debug
```
    alembic upgrade head
    uvicorn app.main:app --reload
```

## Migration

```
alembic revision --autogenerate -m "Add column last_name to User model"
alembic upgrade head
```