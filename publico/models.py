from enum import Enum
from django.db import models

class contatoTipo(Enum):
    EMAIL = "E-mail"
    CELULAR = "Celular"
    INSTAGRAM = "insta"
    @classmethod
    def choices(cls):
        return [( key.name, key.value) for key in cls]

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField( max_length=260, unique=True)
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    email =  models.CharField(max_length=200)

    def get_contatos(self):
        return self.contato_set.all()

class contato(models.Model):
    tipo = models. CharField(choices=contatoTipo.choices(), max_length=100)
    valor = models.CharField(max_length=200)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Endereco(models.Model):
    uf = models.CharField(max_length=2)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    numero = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)
    complemento = models.TextField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
