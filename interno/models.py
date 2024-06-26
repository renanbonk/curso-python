from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

class Estado(models.Model):    
    nome = models.CharField(max_length=100, unique=True)
    sigla = models.CharField(max_length=2, unique=True)

class Produto(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to="produtos_imagem", null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Nome: {self.nome} Categoria: {self.categoria.nome}"

    
# class Cidades(models.Model):
#     nome = models.CharField(max_length=100, unique=True)
#     quantidade_habitantes = models.DecimalField(max_digits=10, decimal_places=10)
#     clima = models.CharField()
#     data_fundacao = models.DateField()
#     estado= models.ForeignKey(Estado, on_delete=models.CASCADE)

#     def __str__(self) -> str:
#         return f"nome: {self.nome} Estado: {self.estado.nome}"