from .Veiculo import Veiculo

class Motocicleta(Veiculo):
    def __init__(self, nome: str, ano: int,
                 diaria: float, cilindrada: int):
        super().__init__(nome, ano, diaria)
        self.__cilindrada = cilindrada
        
    
    @property
    def cilindrada(self):
        return self.__cilindrada
    
    
    @cilindrada.setter
    def cilindrada(self, nova_cilindrada):
        self.__cilindrada = nova_cilindrada
        
    
    def __str__(self):
        return super().__str__() + f' - Cilindrada: {self.cilindrada}cc'
        
    
    def calcular_aluguel(self, n_dias, desconto=0):
        if self.cilindrada >= 200:
            self.diaria += 20
        
        
        return super().calcular_aluguel(n_dias, desconto)