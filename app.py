from flask import Flask, render_template, request

app = Flask()

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
    return render_template('veiculos.html')


if __name__ == '__main__':
    app.run()