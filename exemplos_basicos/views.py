from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request) -> HttpResponse:
    response = HttpResponse(content="""
        <h1> Hello Word </h1>
        <a href="contato">Contato</a>
        <a href="/exemplos-basicos/jogo">Jogo</a>                  
        <a href="/exemplos-basicos/calculadora-form">Calculadora</a>                  
        <a href="/exemplos-basicos/sobre-form">Sobre</a>                  
        <a href="/exemplos-basicos/carros-form">Carros</a>                  
         """)
    return response


def contato(request) -> HttpResponse:
    template = loader.get_template(template_name="contato.html")
    html = template.render(context={}, request=request)
    response = HttpResponse(content=html)
    return response

def jogo(request) -> HttpResponse:
    return render(request,"jogo.html")

def calculadora(request, numero1: int=3, numero2: int=8) -> HttpResponse:
    soma = numero1+numero2
    contexto_dados = {
        "n1": numero1,
        "n2": numero2,
        "soma": soma
    }
    return render(request, "calculadora.html",context=contexto_dados)

def sobre (request) -> HttpResponse:
    nome = "Renan"
    sobrenome = "Bonk"
    nome_completo = nome + sobrenome
    idade = 27
    ano_nascimento = 2024 - idade
    peso = 73
    altura = 1.73
    imc = peso/(altura*altura)

    contexto_dados = {
        "nome": nome,
        "sobrenome": sobrenome,
        "nomeCompleto": nome_completo,
        "idade": idade,
        "AnoNascimento": ano_nascimento,
        "peso": peso,
        "altura": altura,
        "imc": imc
    }
    return render(request, "sobre.html",context=contexto_dados)



def calculadora_form(request):
    if request.method == "POST":
        numero1= int(request.POST.get("numero1"))
        numero2= int(request.POST.get("numero2"))
        operacao = request.POST.get("operacao")

        match(operacao):
            case "somar": resultado = numero1+numero2
            case "subtrair": resultado = numero1-numero2
            case "multiplicar": resultado = numero1*numero2
            case "dividir": resultado = numero1/numero2
    else:
        resultado = None
    return render(request,"calculadora-form.html", context={"resultado": resultado})

def calcular(request):
    numero1= int(request.GET.get("numero1"))
    numero2= int(request.GET.get("numero2"))
    operacao = request.GET.get("operacao")

    match(operacao):
        case "somar": resultado = numero1+numero2
        case "subtrair": resultado = numero1-numero2
        case "multiplicar": resultado = numero1*numero2
        case "dividir": resultado = numero1/numero2

    return HttpResponse(f"Resultado: {resultado}")



def sobre_form(request):
    return render(request, "sobre-form.html")

def cadastrar(request):

    nome=str(request.GET.get("nome"))
    sobrenome=str(request.GET.get("sobrenome"))
    idade=int(request.GET.get("idade"))
    peso=float(request.GET.get("peso"))
    altura=float(request.GET.get("altura"))

    nome_completo = nome+" "+sobrenome
    ano_nascimento = 2024-idade
    imc = peso/(altura*altura)

    #return HttpResponse (f"Nome Completo: {nome_completo} <br> Ano Nascimento: {ano_nascimento} <br> Peso: {peso} <br> Altura: {altura} <br> Imc: {imc}" )


    contexto_dados = {
        "nome": nome,
        "sobrenome": sobrenome,
        "nome_completo": nome_completo,
        "ano_nacimento": ano_nascimento,
        "idade": idade,
        "peso": peso,
        "altura": altura,
        "imc": imc,
    }

    return render(request, "sobre.html", context=contexto_dados)


def carros_form(request):
    return render(request, "carros-form.html")

def cadastrar_carros(request):
    modelo = (request.POST.get("modelo"))
    preco = (request.POST.get("preco"))
    ano_fabricacao = (request.POST.get("ano_fabricacao"))
    cor = (request.POST.get("cor"))

    contexto_dados = {
        "modelo": modelo,
        "preco": preco,
        "ano_fabricacao": ano_fabricacao,
        "cor": cor
    }

    return render(request, "carros.html", context=contexto_dados)
