const element = document.getElementById('id_cep');
const maskOptions = {
  mask: '00.000-000'
};
const mask = IMask(element, maskOptions);

function consultarCep(elemento){
  let inputCep = elemento.target;
  let cep = inputCep.value.replace(".", "").replace("-", "");
  if (cep.length !==8)
    return

  fetch(`https://viacep.com.br/ws/${cep}/json/`)
    .then((response) =>response.json())
    .then((data) =>{
        if(data["error"] === "true"){
            alert("CEP inexistente")
            document.getElementById("id_cep").focus()
            document.getElementById("id_cep").select()
            return
        }
      document.getElementById("id_uf").value = data["uf"]
      document.getElementById("id_cidade").value = data["localidade"]
      document.getElementById("id_bairro").value = data["bairro"]
      document.getElementById("id_rua").value = data["logradouro"]
      document.getElementById("id_numero").focus()
    })
    .catch((error)=>{
      alert("não foi possivel buscar o endereço")
      console.error(error)
    })
}

document.getElementById("id_cep").onkeyup = consultarCep;

function submitFormDadosEndereco(event) {
    let form = document.getElementById("form-endereco");

    if (!form.checkValidity()){
        let invalido = form.querySelector(":invalid")
        invalido.reportValidity();
        return;
    }
    form.submit()
}



document.getElementById("form-endereco-botao-cadastrar").onclick = submitFormDadosEndereco