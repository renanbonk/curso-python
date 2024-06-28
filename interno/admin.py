from django.contrib import admin

from interno.models import Categoria, Produto


# Register your models here.
class CategoriaAdimin(admin.ModelAdmin):
    list_display = ('nome', )

class ProdutoAdimin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'preco' )

admin.site.register(Categoria, CategoriaAdimin)
admin.site.register(Produto, CategoriaAdimin)