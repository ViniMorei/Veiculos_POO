from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager

from classes.Veiculo import Veiculo
from classes.Carro import Carro
from classes.Motocicleta import Motocicleta

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def instanciar_carro(nome: str, ano: int, diaria: float, combustivel: str):
    return Carro(nome, ano, diaria, combustivel)


def instanciar_moto(nome: str, ano: int, diaria: float, cilindrada: int):
    return Motocicleta(nome, ano, diaria, cilindrada)


def processar_form(form_veiculo: dict):
    nome = form_veiculo['nome']
    ano = form_veiculo['ano']
    diaria = form_veiculo['diaria']

    if 'combustivel' in form_veiculo:
        combustivel = form_veiculo['combustivel']
        carro = instanciar_carro(nome, ano, diaria, combustivel)
        id = Veiculo.veiculos_cadastrados
        linha = f'{id},{carro.nome},{carro.ano},{carro.diaria},{carro.__class__.__name__},{carro.combustivel}, '

    elif 'cilindrada' in form_veiculo:
        cilindrada = form_veiculo['cilindrada']
        moto = instanciar_moto(nome, ano, diaria, cilindrada)
        id = Veiculo.veiculos_cadastrados
        linha = f'{id},{moto.nome},{moto.ano},{moto.diaria},{moto.__class__.__name__}, ,{moto.cilindrada}'

    
    escrever_linha('veiculos.txt', linha)


def escrever_linha(nome_arquivo: str, linha: str):
    with open(nome_arquivo, 'a') as arquivo:
        arquivo.write(linha)


def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()
    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()

    try:
        pass
    
    except Exception as ex:
        print(ex)
        
    finally:
        bot.wait(3000)
        bot.stop_browser()


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
