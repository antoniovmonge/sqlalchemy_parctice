# SQLAlchemy + PostgreSQL + Alembic + Docker + pgAdmin

This project

```bash
docker-compose up
```

```bash
docker-compose down
```

pgAdmin

<http://localhost:8080>

## Load the products

The products.csv file must be included in a folder called Data that is include in the `.gitignore` file

```bash
python import_products.py
```
