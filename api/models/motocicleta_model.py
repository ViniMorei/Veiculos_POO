from sqlalchemy import Integer, Float, String
from sqlalchemy.orm import Mapped, mapped_column

from api.models.base import Base


class Motocicleta(Base):
    __tablename__ = 'motocicletas'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    ano: Mapped[int] = mapped_column(Integer, nullable=False)
    diaria: Mapped[float] = mapped_column(Float, nullable=False)
    cilindradas: Mapped[int] = mapped_column(Integer, nullable=False)


    def __repr__(self):
        return f'<Moto(id={self.id}, nome="{self.nome}", ano={self.ano}, diaria={self.diaria}, cilindradas="{self.cilindradas}")>'