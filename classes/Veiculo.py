class Veiculo:
    veiculos_cadastrados = 0
    
    def __init__(self, nome: str, ano: int, diaria: float):
        self.__nome = nome
        self.__ano = ano
        self.__diaria = diaria
        Veiculo.veiculos_cadastrados += 1
        
    
    @property
    def nome(self):
        return self.__nome
    
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
    
    
    @property
    def ano(self):
        return self.__ano
    
    
    @ano.setter
    def ano(self, novo_ano):
        self.__ano = novo_ano
    
    
    @property
    def diaria(self):
        return self.__diaria
    
    
    @diaria.setter
    def diaria(self, nova_diaria):
        self.__diaria = nova_diaria
        
        
    def __str__(self):
        return f'Veículo: {self.nome} {self.ano} - Valor da diária: R${self.diaria}'
        
        
    def calcular_aluguel(self, n_dias: int, desconto=0):
        return self.diaria * n_dias - desconto
    
    
    @classmethod
    def total_veiculos(cls, veiculos: list):
        if cls.veiculos_cadastrados:
            print(f'\n{cls.veiculos_cadastrados} veículos alugados: \n')
            for index, veiculo in enumerate(veiculos):
                print(f'{index + 1} - {veiculo.__str__()}')
        else:
            print('\nNão há veículos alugados!')
    
    
    @classmethod
    def aplicar_aumento(cls, veiculos: list, aumento: float):
        for veiculo in veiculos:
            novo_valor = veiculo.diaria + aumento
            veiculo.diaria = novo_valor