import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


MYSQL_USER="root"
MYSQL_PASSWORD="bita1986"
MYSQL_SERVER="localhost"
MYSQL_PORT="3306"
MYSQL_DB="medios_federales"

DATABASE_URL=f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_SERVER}/{MYSQL_DB}'

engine = create_engine(
    DATABASE_URL, pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
