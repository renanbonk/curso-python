from django.shortcuts import render, redirect
from . import models


def home(request):
    return render(request,"home.html")


def categoria_index(request):
    categorias = models.Categoria.objects.all()
    property(categorias)
    contexto={
        "categorias": categorias
    }
    return render(request,"categorias/index.html", context=contexto)


def categoria_cadastrar(request):
    if request.method == "GET":
        return render(request,"categorias/cadastrar.html")
    
    nome = request.POST.get("nome").strip()
    categoria=models.Categoria(nome=nome)
    categoria.save()
    return redirect("categorias")


def categoria_apagar(request, id: int):
    categoria = models.Categoria.objects.get(pk=id)
    categoria.delete()

    return redirect ("categorias")

def categoria_editar(request, id: int):
    categoria = models.Categoria.objects.get(pk=id)
    if request.method == "GET":
        contexto = {"categoria": categoria}
        return render(request,"categorias/editar.html", context=contexto)
    
    categoria.nome = request.POST.get("nome").strip()
    categoria.save()
    return redirect ("categorias")


def estado_index(request):
    estados = models.Estado.objects.all()
    property(estados)
    contexto ={
        "estados": estados
    }
    return render(request,"estados/index.html", context=contexto)
    

def estado_cadastrar(request):
    if request.method == "GET":
        return render (request,"estados/cadastrar.html")
    
    nome= request.POST.get("nome").strip()
    uf=request.POST.get("uf")
    estado=models.Estado(nome=nome, sigla=uf)
    estado.save()
    return redirect("estados")


def estado_apagar(request, id: int):
    estado=models.Estado.objects.get(pk=id)
    estado.delete()
    return redirect("estados")


def estado_editar(request, id: int):
    estado = models.Estado.objects.get(pk=id)
    if request.method == "GET":
        contexto ={"estado": estado}
        return render(request, "estados/editar.html", context=contexto)
    estado.nome = request.POST.get("nome").strip()
    estado.save()
    return redirect ("estados")

# Create your views here.