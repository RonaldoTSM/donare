from django.db import models
from app_criar_perfil_ong.models import CadastroOng  

class Publicacao(models.Model):
    autor = models.ForeignKey(CadastroOng, on_delete=models.CASCADE, related_name='publicacoes')
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = 'publicacoes'