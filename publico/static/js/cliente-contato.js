const botoesEditarContato = document.getElementsByClassName("botao-editar-contato");
Array.from(botoesEditarContato).forEach((botao) => {
    botao.onclick = obterDadosContato
});

function obterDadosContato(elementoDoClick) {
    // Obter o id que foi preenchido no atributo data-id do botão editar da lista de contatos
    let idContato = elementoDoClick.target.getAttribute("data-id")
    // Requisição para obter os dados do contato
    fetch(`/publico/contato/${idContato}`)
        .then(response => response.json())
        .then(data => {
            console.log(data)
            // Preencher os campos com os dados da requisição para usuário poder alterar 
            document.getElementById("id_valor").value = data.valor
            document.getElementById("id_tipo").value = data.tipo
            document.getElementById("form-contato").action = `/publico/contato/editar/${idContato}`
            document.getElementById("form-contato-botao-cadastrar").innerHTML = "alterar"

            const modal = document.getElementById(document.querySelectorAll('.js-modal-trigger')[0].dataset.target)
            modal.classList.add("is-active")
        })

        .catch(error => {
            console.log(error)
            alert("Ocorreu um erro ao carregar os dados do contato")
        })
}



function submitFormDadosContato(event) {
    document.getElementById("form-contato").submit()
}


document.getElementById("form-contato-botao-cadastrar").onclick = submitFormDadosContato





