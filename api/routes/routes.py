from flask import Blueprint, render_template, request, jsonify
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

    VeiculoService.add_carro(nome=nome, ano=ano, diaria=diaria, combustivel=combustivel)
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
    
    VeiculoService.add_moto(nome=nome, ano=ano, diaria=diaria, cilindradas=cilindrada)
    processar_form(moto)
    
    return listar_veiculos()
    

# Rotas de PUT
@routes.route('/atualizar_veiculo/<int:id_veiculo>', methods=['PUT'])
def atualizar_veiculo(id_veiculo: int):
    novos_dados = request.json
    veiculo = VeiculoService.update_veiculo(id_veiculo, novos_dados)

    if veiculo:
        return jsonify({'mensagem' : 'Veículo atualizado com sucesso!'}), 200
    else:
        return jsonify({'mensagem' : 'Veículo não encontrado.'}), 404


# Rotas de DELETE
@routes.route('/excluir_veiculo/<int:id_veiculo>', methods=['DELETE'])
def excluir_veiculo(id_veiculo: int):
    sucesso = VeiculoService.delete_veiculo(id_veiculo)

    if sucesso:
        return jsonify({'mensagem' : 'Veículo excluído com sucesso!'}), 200
    else:
        return jsonify({'mensagem' : 'Veículo não encontrado.'}), 404