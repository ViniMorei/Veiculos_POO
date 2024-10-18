from api.config.database import Session
from api.models import Veiculo, Carro, Motocicleta


# Definição das funções e lógica que 
# será utilizada dentro das rotas
class VeiculoService():

    # Recupera todos os veículos cadastrados
    @classmethod
    def get_all():
        with Session() as session:
            try:
                veiculos = session.query(Veiculo).all()
                return veiculos
            
            except Exception as ex:
                print(f'Erro ao recuperar os veículos: {ex}')

            finally:
                session.close()
        
    
    # Recupera só um veículo, a partir da chave primária
    @classmethod
    def get_by_id(id_veiculo: int):
        with Session() as session:
            try:
                veiculo = session.query(Veiculo).filter(Veiculo.id == id_veiculo).first()
                return veiculo
            
            except Exception as ex:
                print(f'Erro ao recuperar veículo: {ex}')

            finally:
                session.close()
        
    
    # Cria uma instância de Carro no BD
    @classmethod
    def add_carro(nome: str, ano: int, diaria: float, combustivel: str):
        with Session() as session:
            novo_carro = Carro(
                nome=nome,
                ano=ano,
                diaria=diaria,
                combustivel=combustivel,
                tipo='Carro'
            )

            try:
                session.add(novo_carro)
                session.commit()

            except Exception as ex:
                session.rollback()
                print(f'Erro ao adicionar Carro: {ex}')

            finally:
                session.close()


    # Cria uma instância de Moto no BD
    @classmethod
    def add_carro(nome: str, ano: int, diaria: float, cilindradas: int):
        with Session() as session:
            nova_moto = Motocicleta(
                nome=nome,
                ano=ano,
                diaria=diaria,
                cilindradas=cilindradas,
                tipo='Moto'
            )

            try:
                session.add(nova_moto)
                session.commit()

            except Exception as ex:
                session.rollback()
                print(f'Erro ao adicionar Moto: {ex}')

            finally:
                session.close()
