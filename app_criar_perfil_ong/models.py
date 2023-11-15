from django.db import models

class CadastroOng(models.Model):
    nome = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    cnpj = models.CharField(max_length=20, unique=True)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(max_length=100, unique=True)
    senha = models.CharField(max_length=50)

    class Meta:
        db_table = 'dados-cadastrais-ong'
