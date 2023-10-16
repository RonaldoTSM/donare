from django.db import models

class Cadastro(models.Model):
    Nome = models.CharField(max_length=50)
    username = models.CharField(max_length=100, unique=True)
    senha = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    telefone = models.CharField(max_length=11)

    class Meta:
        db_table = 'dados-cadastrais-doador'

