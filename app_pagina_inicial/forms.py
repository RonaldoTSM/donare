from django import forms
from .models import Publicacao, Doacoes

class PublicacaoForm(forms.ModelForm):
    class Meta:
        model = Publicacao
        fields = ['titulo', 'descricao']
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Digite o título aqui'}),
            'descricao': forms.Textarea(attrs={'placeholder': 'Descreva sua publicação'}),
        }

class DoacaoForm(forms.ModelForm):
    class Meta:
        model = Doacoes
        fields = ['forma_pagamento', 'valor']
