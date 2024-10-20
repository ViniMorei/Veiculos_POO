/* Script carregado na tabela de veiculos.html, para executar 
   as funções específicas de objeto declarado nas classes Veiculo.py,
   Carro,py e Motocicleta.py (módulo classes). O objetivo é instanciar
   essas classes para executar essas funcionalidades
*/

// Função que exibe o modal expandindo os detalhes do veículo
function abrirModal(button){
    var id = button.getAttribute('dado-id');
    var nome = button.getAttribute('dado-nome');
    var ano = button.getAttribute('dado-ano');
    var diaria = button.getAttribute('dado-diaria');
    var tipo = button.getAttribute('dado-tipo');
    var combustivel = button.getAttribute('dado-combustivel');
    var cilindradas = button.getAttribute('dado-cilindradas');

    document.getElementById('modal-id').innerText = id;
    document.getElementById('modal-nome').value = nome;
    document.getElementById('modal-ano').value = ano;
    document.getElementById('modal-diaria').value = diaria;
    document.getElementById('modal-tipo').value = tipo;
    document.getElementById('modal-combustivel').value = combustivel;
    document.getElementById('modal-cilindradas').value = cilindradas;

    var modal = document.getElementById('detalhesModal');
    $('#detalhesModal').modal('show');
    modal.style.display = 'flex';
    

    var span = document.getElementsByClassName('close')[0];
    span.onclick = function(){
        modal.style.display = 'none';
    }

    var inputCombustivel = document.getElementById('modal-combustivel');
    var inputCilindradas = document.getElementById('modal-cilindradas');

    if (tipo == 'Carro'){
        inputCombustivel.disabled = false;
        inputCilindradas.disabled = true;
    } else if (tipo == 'Moto'){
        inputCilindradas.disabled = false;
        inputCombustivel.disabled = true;
    } else{
        inputCombustivel.disabled = true;
        inputCilindradas.disabled = true;
    }
}


function fecharModal(){
    var modal = document.getElementById('detalhesModal');
    modal.style.display = 'none';
}


// Função que permite acessar um endpoint que edita os dados do veículo a partir do ID
function editarItem(){
    var id = document.getElementById('modal-id').innerText;
    var nome = document.getElementById('modal-nome').value;
    var ano = document.getElementById('modal-ano').value;
    var diaria = document.getElementById('modal-diaria').value;
    var tipo = document.getElementById('modal-tipo').value;

    var combustivel = document.getElementById('modal-combustivel').value;
    var cilindradas = document.getElementById('modal-cilindradas').value;

    var dados = {
        id: id,
        nome: nome,
        ano: ano,
        diaria: diaria,
        tipo: tipo,
    };
    if (tipo === 'Carro'){
        dados.combustivel = combustivel;
    } else if (tipo === 'Moto'){
        dados.cilindradas = cilindradas;
    }

    // Enviar a requisição HTTP
    if (confirm('Tem certeza que quer alterar esse veículo?')){
        fetch(`/atualizar_veiculo/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(dados),
        })
        .then(response => response.json())
        .then(data => {
            if (data.mensagem){
                alert(data.mensagem);
                $('#detalhesModal').modal('hide');
                location.reload();
            } else{
                alert('Erro!');
            }
        });
    }
}


// Função que exclui o item a partir do ID
function excluirItem(){
    var id = document.getElementById('modal-id').innerText;

    if (confirm('Tem certeza que deseja excluir este item?')){
        fetch(`/excluir_veiculo/${id}`, {
            method: 'DELETE'
        })
        .then(response => response.json())
        .then(data => {
            if (data.mensagem){
                alert(data.mensagem);
                $('#detalhesModal').modal('hide');
                location.reload();
            } else{
                alert('Erro!');
            }
        });
    }
}


// Calcula o aluguel do veículo a partir da quantidade de dias inputada pelo usuário
function calcularAluguel(){

}


// Aplica um aumento na taxa diária do veículo
function aplicarAumento(){

}
