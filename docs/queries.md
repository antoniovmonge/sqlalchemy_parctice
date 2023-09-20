# Queries

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

```bash
q = (
    select(Product)
        .where(Product.manufacturer == 'Commodore')
        .where(Product.year == 1980)
)
```

```bash
q = (
    select(Product)
        .where(
            Product.manufacturer == 'Commodore',
            Product.year == 1980
        )
)
```

```bash
from sqlalchemy import or_
q = (
    select(Product)
        .where(
            or_(
                Product.year < 1970,
                Product.year > 1990
            )
        )
)
```

```bash
q = select(Product).where(Product.name.like('%Sinclair%'))
```

```bash
q = select(Product).where(Product.year.between(1970, 1979))
```

```bash
q = select(Product).where(Product.id == 23)
session.scalar(q)
```
