from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from publico import models
from publico.forms import ClienteCadastroForm, ClienteEditarDetalheForm, ContatoCadastroForm, EnderecoCadastroForm


# Create your views here.
def cliente_cadastrar(request):
    if request.method == "POST":
        form = ClienteCadastroForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            return redirect("cliente_detalhe", id=cliente.id)

    form = ClienteCadastroForm()
    contexto = {"form": form}
    return render(request, "clientes/cadastrar.html", contexto)


def cliente_detalhe(request, id: int):
    cliente = get_object_or_404(models.Cliente, id=id)
    if request.method == "POST":
        form_cliente = ClienteEditarDetalheForm(request.POST, request.FILES, instance=cliente)
        if form_cliente.is_valid():
            form_cliente.save()

    contatos = cliente.get_contatos()
    enderecos = cliente.get_enderecos()

    form_cliente = ClienteEditarDetalheForm(instance=cliente)
    form_endereco = EnderecoCadastroForm()
    form_contato = ContatoCadastroForm()

    registro_criado = request.session.get("registro_criado")
    registro_criado_mensagem = request.session.get("registro_criado_mensagem")
    if registro_criado:
        request.session.pop("registro_criado")
        request.session.pop("registro_criado_mensagem")

    contexto = {
        "cliente": cliente,
        "contatos": contatos,
        "enderecos": enderecos,
        "form_contato": form_contato,
        "form": form_cliente,
        "form_endereco": form_endereco,
        "registro_criado": registro_criado,
        "registro_criado_mensagem": registro_criado_mensagem,
    }
    return render(request, "clientes/detalhe.html", contexto)


def contato_cadastrar(request, id_cliente: int):
    cliente = get_object_or_404(models.Cliente, id=id_cliente)
    form = ContatoCadastroForm(request.POST)
    contato = form.save(commit=False)
    contato.cliente = cliente
    contato.save()
    return redirect("cliente_detalhe", id=cliente.id)


def contato_apagar(request, id: int):
    contato = get_object_or_404(models.contato, id=id)
    id_cliente = contato.cliente.id
    contato.delete()
    return redirect("cliente_detalhe", id=id_cliente)


def contato_detalhe(request, id: int):
    contato = get_object_or_404(models.contato, id=id)
    return JsonResponse(model_to_dict(contato))


def contato_editar(request, id: int):
    contato = get_object_or_404(models.contato, id=id)
    form = ContatoCadastroForm(request.POST, instance=contato)
    contato = form.save()
    return redirect("cliente_detalhe", contato.cliente.id)


def endereco_cadastrar(request, id_cliente: id):
    cliente = get_object_or_404(models.Cliente, id=id_cliente)
    form = EnderecoCadastroForm(request.POST)
    endereco = form.save(commit=False)
    endereco.cliente = cliente
    endereco.save()
    request.session['registro_criado']=True
    request.session['registro_criado_mensagem'] = "Endereço criado com sucesso"
    return redirect("cliente_detalhe", id=cliente.id)


def endereco_editar(request, id: int):
    pass


def endereco_apagar(request, id: int):
    endereco = get_object_or_404(models.Endereco, id=id)
    id_cliente = endereco.cliente.id
    endereco.delete()
    return redirect("cliente_detalhe", id=id_cliente)
