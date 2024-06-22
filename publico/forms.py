from django import forms
from . import models

class ClienteCadastroForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields= ['nome', 'cpf', 'data_nascimento', 'email']

class ContatoCadastroForm(forms.ModelForm):
    class Meta:
        model = models.contato
        fields = ["tipo", "valor"]        