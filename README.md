# plough
backend for little plough

## Migration

```
alembic revision --autogenerate -m "Add column last_name to User model"
alembic upgrade head
```