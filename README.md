# Botcity Orientado a Objetos - Veículos

Este projeto utiliza o conceito de orientação a objetos em _Python_ e uma _API_ _Flask_ para gerenciar um sistema de aluguel de veículos (carros e motocicletas). São utilizadas diferentes rotas em cada template para instanciar um objeto das classes Carro ou Motocicleta ao utilizar o _submit_ do formulário _HTML_. Ao final da execução, os objetos estarão em um arquivo txt e na própria aplicação _Flask_.

## Início

Estas instruções detalham o fluxo que deve ser seguido para poder executar esta automação.

### Pré-requisitos
- Ter o _Python_ instalado na máquina

### Execução
* Criar um ambiente virtual para instalar as dependências:
  ```
  python -m venv venv
  venv/Scripts/Activate
  
  (venv) pip install -r requirements.txt
  ```

* Dividir o terminal do _VS Code_ (ou abrir dois terminais diferentes):
  - No primeiro terminal, rode a API:
    ```
    python app.py 
    ```
  - No segundo terminal, rode a automação:
    ```
    python bot.py
    ```