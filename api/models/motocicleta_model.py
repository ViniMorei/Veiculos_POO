from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from api.models.veiculo_model import Veiculo


class Motocicleta(Veiculo):
    __tablename__ = 'motocicletas'

    id: Mapped[int] = mapped_column(ForeignKey('veiculos.id'), primary_key=True)
    cilindradas: Mapped[int] = mapped_column(Integer, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity' : 'Moto'
    }


    def __repr__(self):
        return f'<Moto(id={self.id}, nome="{self.nome}", ano={self.ano}, diaria={self.diaria}, cilindradas="{self.cilindradas}")>'