from django.urls import path
from.import views

urlpatterns = [
    path("/home", views.index),
    path("/", views.index),
    path("/contato", views.contato),
    path("/jogo", views.jogo),
    path("/calculadora", views.calculadora),
    path("/sobre", views.sobre),
    path("/calculadora/numero1/<int:numero1>", views.calculadora),
    path("/calculadora/numero1/<int:numero1>/numero2/<int:numero2>", views.calculadora),
    path("/calculadora-form", views.calculadora_form),
    path("/calcular", views.calcular),
    path("/sobre-form", views.sobre_form),
    path("/cadastrar", views.cadastrar),
    path("/cadastrar-carros", views.cadastrar_carros),
    path("/carros-form", views.carros_form),
]