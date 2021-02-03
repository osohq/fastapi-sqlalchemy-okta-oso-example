from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///bear.db", connect_args={"check_same_thread": False})

Base = declarative_base()


def setup_db():
    # Reset database.
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
