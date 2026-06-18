

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import config

engine = create_engine(config.db_name, connect_args={'check_same_thread': False}, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()
