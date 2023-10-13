# Create your views here.

from django.shortcuts import render

def criar_perfil_ong(request):
    return render(request, 'cadastro_ong/perfil_ong.html')

def dados_bancarios_ong(request):
    return render(request, 'cadastro_ong/dados_bancarios.html')
