from django.db import models

class Cadastro(models.Model):
    Nome = models.CharField(max_length=50)
    username = models.CharField(max_length=100, unique=True)
    senha = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    telefone = models.CharField(max_length=11)
    nascimento = models.CharField(max_length=8)
    descricao = models.CharField(max_length=500)
    rua = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cep = models.CharField(max_length=9)
    interesses = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'dados-cadastrais-doador'

