from sqlalchemy import (
    create_engine , 
    URL 
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import config

DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    host=config.HOST,
    port=config.PORT,
    username=config.USER,
    password=config.PASSWORD,
    database=config.DBNAME
)

engine = create_engine(DATABASE_URL)

BASE = declarative_base()

Session = sessionmaker(autocommit=False , autoflush=True , bind=engine)