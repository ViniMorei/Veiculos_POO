from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.models.base import Base


DATABASE_URL = 'mysql://root:@localhost:3306/veiculos'


engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine, autoflush=False)


def session():
    return Session


def init_db():
    Base.metadata.create_all(bind=engine)
