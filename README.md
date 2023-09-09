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

## Queries

Run in terminal.

```bash
ipython
```

```bash
from db import Session
from models import Product

session = Session()

from sqlalchemy import select
q = select(Product)
```

```bash
print(q)
```

```bash
r = session.execute(q)
list(r)
```

```bash
session.execute(q).all()
```

```bash
session.scalars(q).all()
```
