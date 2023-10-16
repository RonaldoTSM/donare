# Create your views here.

from django.shortcuts import render

def criar_perfil_doador_interesses(request):
    return render(request, 'cadastro_doador/interesses.html')

def criar_perfil_doador(request):
    return render(request, 'cadastro_doador/perfil_doador.html')


