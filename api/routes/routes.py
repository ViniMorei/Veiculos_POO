from flask import Blueprint, render_template, request
from automation.bot import processar_form
from api.services import VeiculoService

routes = Blueprint('routes', __name__)


# Rotas de template
@routes.route('/')
def index():
    return render_template('index.html')


@routes.route('/alugar_carros')
def alugar_carros():
    return render_template('carro.html')


@routes.route('/alugar_motos')
def alugar_motos():
    return render_template('moto.html')


@routes.route('/listar_veiculos')
def listar_veiculos():
    dados = VeiculoService.get_all()
    return render_template('veiculos.html', dados=dados)


# Rotas de POST
@routes.route('/alugar_carros/instanciar', methods=['POST'])
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
    
    return listar_veiculos()


@routes.route('/alugar_motos/instanciar', methods=['POST'])
def alugar_motos_instanciar():
    nome = request.form['nome']
    ano = request.form['ano']
    diaria = request.form['diaria']
    cilindrada = request.form['cc']

    moto = {
        'nome' : nome,
        'ano' : ano,
        'diaria' : diaria,
        'cilindrada' : cilindrada
    }
    
    processar_form(moto)
    
    return listar_veiculos()
    