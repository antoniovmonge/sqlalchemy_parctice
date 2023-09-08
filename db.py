import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase


load_dotenv(".envs/.env_db")


# print('Database URL:', os.getenv('DATABASE_URL'))
engine = create_engine(os.getenv('DATABASE_URL'), echo=True)

class Model(DeclarativeBase):
    pass
