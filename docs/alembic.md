# Alembic

```bash
alembic init migrations
```

Configure necessary files.

```bash
alembic revision --autogenerate -m "products, manufacturers, countries"
```

```bash
alembic upgrade head
```
