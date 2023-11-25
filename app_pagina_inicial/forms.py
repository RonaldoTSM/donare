from django import forms
from .models import Publicacao

class PublicacaoForm(forms.ModelForm):
    class Meta:
        model = Publicacao
        fields = ['titulo', 'descricao']
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Digite o título aqui'}),
            'descricao': forms.Textarea(attrs={'placeholder': 'Descreva sua publicação'}),
        }
