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

## Create DB with pgAdmin

### 1. Add New Server

#### "General" Tab

**Name:** db

#### "Connection" tab

**Host name:** db

**Port:** 5432

**Maintenance database:** postgres

**Username:** postgres

**Password:** POSTGRES_PASSWORD (from .env)

**Save password?**: yes

[SAVE]

### 2. Create the user

Create a dedicated user for each database.

Right click on `db` -> `Create` -> `Login/Group Role...`

#### "General" tab

**Name:** [name for the user]

#### "Definition" tab

**Password:** [password for the user]

#### "Privileges" tab

**Can login?:** yes

[SAVE]

### 3. Create the DataBase

Right click on `Databases` -> `Create` -> `Database...`

#### "General" tab

**Name:** [name for the database] (same as the user)

### 4. Configure privileges

`db` -> `Databases` -> `(name of just created db)` -> `Schemas` -> `public`

Right click on the `public` schema and select `Properties...`

#### "Security" tab

1. Click on `+` button in the "Privileges" section.
2. Under "Grantee" select the name of the created "user"
3. In the "Privileges" column select `all`

[SAVE]
