from django.urls import path
from . import views


urlpatterns = [
    path("/", views.home, name="interno_home"),
    path("/categoria", views.categoria_index, name="categorias"),
    path("/categoria/cadastrar", views.categoria_cadastrar),
    path("/categoria/apagar/<int:id>", views.categoria_apagar),
    path("/categoria/editar/<int:id>", views.categoria_editar),
    path("/estados", views.estado_index, name="estados"),
    path("/estados/cadastrar", views.estado_cadastrar),
    path("/estados/apagar/int:id>", views.estado_apagar),
    path("/estados/editar/int:id>",views.estado_editar),

]