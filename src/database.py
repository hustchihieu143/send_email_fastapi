from src.config import Settings, get_settings
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

db_config = port = os.environ.get("MYSQL_DATABASE_URL")

Base = declarative_base()


def get_db_url() -> str:
    return db_config


engine = create_engine(get_db_url())
DBSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

