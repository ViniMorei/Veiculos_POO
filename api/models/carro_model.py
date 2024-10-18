from sqlalchemy import Column, Integer, String, Float
from api.config.database import Base


class Carro(Base):
    __tablename__ = 'carros'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    ano = Column(Integer, nullable=False)
    diaria = Column(Float, nullable=False)
    combustivel = Column(String(50), nullable=False)