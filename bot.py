from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker

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
        linha = f'{id},{carro.nome},{carro.ano},{carro.diaria},{carro.__class__.__name__},{carro.combustivel}, \n'
        print(linha)

    elif 'cilindrada' in form_veiculo:
        cilindrada = form_veiculo['cilindrada']
        moto = instanciar_moto(nome, ano, diaria, cilindrada)
        id = Veiculo.veiculos_cadastrados
        linha = f'{id},{moto.nome},{moto.ano},{moto.diaria},{moto.__class__.__name__},,{moto.cilindrada}\n'
        print(linha)

    
    escrever_linha('veiculos.txt', linha)


def escrever_linha(nome_arquivo: str, linha: str):
    with open(nome_arquivo, 'a', encoding='utf-8') as arquivo:
        arquivo.write(linha)


def inventar_carros():
    fake = Faker()
    nome = f'{fake.word().capitalize()} {fake.word().capitalize()}'
    ano = fake.year()
    diaria = fake.random_number(digits=3)
    combustivel = fake.random_element(elements=('Gasolina', 'Etanol', 'Diesel', 'GNV', 'Elétrico'))
    
    return nome, ano, diaria, combustivel
    

def inventar_motos():
    fake = Faker()
    nome = f'{fake.word().capitalize()} {fake.word().capitalize()}'
    ano = fake.year()
    diaria = fake.random_number(digits=3)
    cilindradas = fake.random_element(elements=(100, 150, 200, 250))
    
    return nome, ano, diaria, cilindradas
    

def preencher_forms(bot:WebBot, carros: int, motos: int):
    for _ in range(carros):
        bot.browse('http://127.0.0.1:5000')
        bot.wait(500)
        
        alugar_carros = bot.find_element('/html/body/ul/li[1]/a/button', By.XPATH)
        alugar_carros.click()
        bot.wait(500)
        
        nome, ano, diaria, combustivel = inventar_carros()
        input_nome = bot.find_element('//*[@id="nome"]', By.XPATH)
        input_ano = bot.find_element('//*[@id="ano"]', By.XPATH)
        input_diaria = bot.find_element('//*[@id="diaria"]', By.XPATH)
        input_combustivel = bot.find_element('//*[@id="combustivel"]', By.XPATH)
        btn_submit = bot.find_element('/html/body/div[1]/form/input[5]', By.XPATH)
        
        input_nome.send_keys(nome)
        input_ano.send_keys(ano)
        input_diaria.send_keys(diaria)
        input_combustivel.send_keys(combustivel)
        
        btn_submit.click()
        bot.wait(500)

    for _ in range(motos):
        bot.browse('http://127.0.0.1:5000')
        bot.wait(500)
        
        alugar_motos = bot.find_element('/html/body/ul/li[2]/a/button', By.XPATH)
        alugar_motos.click()
        bot.wait(500)
        
        nome, ano, diaria, cilindrada = inventar_motos()
        input_nome = bot.find_element('//*[@id="nome"]', By.XPATH)
        input_ano = bot.find_element('//*[@id="ano"]', By.XPATH)
        input_diaria = bot.find_element('//*[@id="diaria"]', By.XPATH)
        input_cilindrada = bot.find_element('//*[@id="cc"]', By.XPATH)
        btn_submit = bot.find_element('/html/body/div[1]/form/input[5]', By.XPATH)
        
        input_nome.send_keys(nome)
        input_ano.send_keys(ano)
        input_diaria.send_keys(diaria)
        input_cilindrada.send_keys(cilindrada)
        
        btn_submit.click()
        bot.wait(500)
        
    return


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
        print("Automação do aluguel de veículos!")
        carros = int(input('Quantos carros você quer alugar? '))
        motos = int(input('Quantas motos você quer alugar? '))
        preencher_forms(bot, carros, motos)
    
    except Exception as ex:
        print(ex)
        
    finally:
        bot.wait(3000)
        bot.stop_browser()


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
