from sqlalchemy import Integer, Float, String
from sqlalchemy.orm import Mapped, mapped_column

from api.models.base import Base


class Veiculo(Base):
    __tablename__ = 'veiculos'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    ano: Mapped[int] = mapped_column(Integer, nullable=False)
    diaria: Mapped[float] = mapped_column(Float, nullable=False)
    tipo: Mapped[str] = mapped_column(String(50), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity' : 'veiculo',
        'polymorphic_on' : tipo
    }


    def __repr__(self):
        return f'<Veiculo(id={self.id}, nome="{self.nome}", ano={self.ano}, diaria={self.diaria})>'