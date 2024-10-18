from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'mysql://root:@localhost:3306/veiculos'


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()


def session():
    return SessionLocal


def init_db():
    Base.metadata.create_all(bind=engine)

