from django.db import models

class CadastroOng(models.Model):
    nome = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    cnpj = models.CharField(max_length=20, unique=True)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(max_length=100, unique=True)
    senha = models.CharField(max_length=50)
    categoria = models.CharField(max_length=50)
    descricao = models.CharField(max_length=500)
    cep = models.CharField(max_length=9)
    rua = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=20)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

    class Meta:
        db_table = 'dados-cadastrais-ong'

class DadosBancariosOng(models.Model):
    ong_user = models.CharField(max_length=50)
    nome_titular = models.CharField(max_length=50)
    conta = models.CharField(max_length=50)
    agencia = models.CharField(max_length=50)
    banco = models.CharField(max_length=50)
    tipoConta = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    pix = models.CharField(max_length=50)
    obs = models.CharField(max_length=150)

    class Meta:
        db_table = 'ong-dados-bancarios'
