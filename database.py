from sqlalchemy import (
    create_engine , 
    URL ,
    MetaData,
)
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

BASE = MetaData()

Session = sessionmaker(engine)