from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from api.models.veiculo_model import Veiculo


class Carro(Veiculo):
    __tablename__ = 'carros'

    id: Mapped[int] = mapped_column(ForeignKey('veiculos.id'), primary_key=True)
    combustivel: Mapped[str] = mapped_column(String(50), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity' : 'Carro'
    }


    def __repr__(self):
        return f'<Carro(id={self.id}, nome="{self.nome}", ano={self.ano}, diaria={self.diaria}, combustivel="{self.combustivel}")>'