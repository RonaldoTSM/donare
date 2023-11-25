from django.shortcuts import render, get_object_or_404
from app_criar_perfil_ong.models import CadastroOng
from app_criar_perfil_doador.models import Cadastro

def home_ong(request, username):
    ong = get_object_or_404(CadastroOng, username=username)
    return render(request, 'paginas/home_ong.html', {'ong': ong})

def home_doador(request, username):
    doador = Cadastro.objects.get(username=username)
    return render(request, 'paginas/home_doador.html', {'doador': doador})

def edit_doador(request, username):
    doador = Cadastro.objects.get(username=username)
    print(doador.__dict__)
    return render(request, 'paginas/home_doador_edit.html', {'doador': doador})