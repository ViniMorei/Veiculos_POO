from .Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, nome: str, ano: int,
                 diaria: float, combustivel: str):
        super().__init__(nome, ano, diaria)
        self.__combustivel = combustivel
        
    
    @property
    def combustivel(self):
        return self.__combustivel
    
    
    @combustivel.setter
    def combustivel(self, novo_combustivel):
        self.__combustivel = novo_combustivel
        
    
    def __str__(self):
        return super().__str__() + f' - Combustível: {self.combustivel}'
        
    
    def calcular_aluguel(self, n_dias, desconto=0):
        if n_dias >= 7:
            desconto = 70
        
        return super().calcular_aluguel(n_dias, desconto)
    
    