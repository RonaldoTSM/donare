from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    usuario = models.CharField(max_length=100, unique=True)
    senha = models.CharField(max_length=50)  # Recomenda-se armazenar senhas de forma segura (hashing e salting).
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    telefone = models.CharField(max_length=11)

    # Adicione outros campos conforme necessário
    # Exemplo: data_nascimento = models.DateField()

    def __str__(self):
        return self.usuario
