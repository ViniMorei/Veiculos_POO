import os

from classes.Veiculo import Veiculo
from classes.Carro import Carro
from classes.Motocicleta import Motocicleta

def main():
    veiculos = []
    menu = '''
Sistema de Aluguel de Veículos
------------------------------
1 - Alugar Carro
2 - Alugar Moto
3 - Listar os veículos alugados
4 - Calcular a diária
5 - Aumentar o valor da diária
0 - Sair

Opção: '''
    
    while True:
        opcao = int(input(menu))
        match(opcao):
            case 0:
                break
            case 1:
                print('ALUGUEL DE CARRO\n--------------')
                nome = input('Qual o nome do carro? ')
                ano = int(input('Qual o ano do carro? '))
                diaria = float(input('Qual o valor da diária? R$'))
                comb = input('Qual o tipo de combustível? ')
                
                carro = Carro(nome, ano, diaria, comb)
                veiculos.append(carro)
                print(f'\nCarro alugado: {carro.__str__()}')
                
            case 2:
                print('ALUGUEL DE MOTO\n--------------')
                nome = input('Qual o nome da moto? ')
                ano = int(input('Qual o ano da moto? '))
                diaria = float(input('Qual o valor da diária? R$'))
                cc = input('Qual o valor das cilindradas? ')
                
                moto = Motocicleta(nome, ano, diaria, cc)
                veiculos.append(moto)
                print(f'\nMoto alugada: {moto.__str__()}')
                
            case 3:
                Veiculo.total_veiculos(veiculos)
            
            case 4:
                if veiculos:
                    Veiculo.total_veiculos(veiculos)
                    indice = int(input('Qual veículo quer calcular? (Índice): ')) - 1
                    try:
                        veiculo = veiculos[indice]
                    except IndexError:
                        print('Índice inválido!')
                        continue
                    
                    dias = int(input('Por quantos dias? '))
                    desconto = float(input('Quanto de desconto? R$'))
                    
                    print(f'Aluguel: R${veiculo.calcular_aluguel(dias, desconto)}')
                
                else:
                    print('Não há veículos para calcular aluguel!')
                
            case 5:
                if veiculos:
                    aumento = float(input('Quanto de aumento nas diárias? R$'))
                    
                    Veiculo.aplicar_aumento(veiculos, aumento)
                    print('Aumento de R${aumento} aplicado!')
                
                else:
                    print('Não há veículos para aplicar aumento!')
            
            case _:
                print('Selecione uma opção válida!')


if __name__ == '__main__':
    main()