# Async Queries

Python shell

```bash
python -m asyncio
```

```bash
from sqlalchemy import select
from db import Session
from models import Product, Customer, Order
session = Session()
```

```bash
c64 = await session.scalar(select(Product).where(Product.name == 'Commodore 64'))
c64
```

```bash
c64.manufacturer
```

```bash
c64.countries
```

Get the last customer in alphabetical order:

```bash
c = await session.scalar(
        select(Customer)
            .order_by(Customer.name.desc())
            .limit(1)
)
c
```

The last two orders from this customer:

```bash
r = await session.scalars(
      c.orders.select()
          .order_by(Order.timestamp.desc())
          .limit(2)
)
r.all()
```

```bash
r = await session.stream_scalars(
      c.orders.select()
          .order_by(Order.timestamp.desc())
          .limit(2)
)
[order async for order in r]
```
