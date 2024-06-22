from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from publico import models
from publico.forms import ClienteCadastroForm, ContatoCadastroForm

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
    contatos=cliente.get_contatos()

    form_contato = ContatoCadastroForm()

    contexto = {"cliente": cliente, "contatos": contatos, "form_contato": form_contato}
    return render(request, "clientes/detalhe.html", contexto)


def contato_cadastrar(request,id_cliente: int):
    cliente = get_object_or_404(models.Cliente, id=id_cliente)
    form = ContatoCadastroForm(request.POST)
    contato =form.save(commit=False)
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
    pass


def endereco_cadastrar(request):
    pass


def endereco_editar(request, id: int):
    pass


def endereco_apagar(request, id: int):
    pass

