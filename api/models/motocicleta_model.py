from sqlalchemy import Column, Integer, String, Float
from api.config.database import Base


class Motocicleta(Base):
    __tablename__ = 'motocicletas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    ano = Column(Integer, nullable=False)
    diaria = Column(Float, nullable=False)
    cilindradas = Column(Integer, nullable=False)