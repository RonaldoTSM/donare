from django.db import models
from app_criar_perfil_ong.models import CadastroOng  
from app_criar_perfil_doador.models import Cadastro

class Publicacao(models.Model):
    autor = models.ForeignKey(CadastroOng, on_delete=models.CASCADE, related_name='publicacoes')
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'publicacoes'

class Doacoes(models.Model):
    autor = models.ForeignKey(Cadastro, on_delete=models.CASCADE, related_name='doacoes')
    ong = models.ForeignKey(CadastroOng, on_delete=models.CASCADE, related_name='doacoes')
    forma_pagamento = models.CharField(max_length=20)
    valor = models.BigIntegerField()
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'doacoes'
