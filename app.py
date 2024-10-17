from flask import Flask, render_template, request
from bot import processar_form

app = Flask(__name__)


def ler_dados():
    with open('veiculos.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    dados = []
    for linha in linhas:
        id, nome, ano, diaria, tipo, comb, cc = linha.strip().split(',')
        dados.append({
            'id' : id,
            'nome' : nome,
            'ano' : ano,
            'diaria' : diaria,
            'tipo' : tipo,
            'combustivel' : comb,
            'cilindradas' : cc
        })
    
    return dados

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/alugar_carros')
def alugar_carros():
    return render_template('carro.html')


@app.route('/alugar_motos')
def alugar_motos():
    return render_template('moto.html')


@app.route('/listar_veiculos')
def listar_veiculos():
    dados = ler_dados()
    return render_template('veiculos.html', dados=dados)


@app.route('alugar_carros/instanciar')
def alugar_carros_instanciar():
    nome = request.form['nome']
    ano = request.form['ano']
    diaria = request.form['diaria']
    combustivel = request.form['combustivel']

    carro = {
        'nome' : nome,
        'ano' : ano,
        'diaria' : diaria,
        'combustivel' : combustivel
    }

    processar_form(carro)


if __name__ == '__main__':
    app.run()