from django.shortcuts import render, get_object_or_404, redirect
from app_criar_perfil_ong.models import CadastroOng
from app_criar_perfil_doador.models import Cadastro
from .forms import PublicacaoForm
from .models import Publicacao

def home_ong(request, username):
    ong = get_object_or_404(CadastroOng, username=username)
    return render(request, 'paginas/home_ong.html', {'ong': ong})

def home_doador(request, username):
    doador = get_object_or_404(Cadastro, username=username)
    return render(request, 'paginas/home_doador.html', {'doador': doador})

def edit_doador(request, username):
    doador = Cadastro.objects.get(username=username)    
    return render(request, 'paginas/home_doador_edit.html', {'doador': doador})

def adicionar_publicacao(request):
    sucesso = False
    if request.method == 'POST':
        form = PublicacaoForm(request.POST)
        if form.is_valid():
            publicacao = form.save(commit=False)
            publicacao.autor = request.user.cadastro  # Ajuste conforme sua associação de usuário
            publicacao.save()
            sucesso = True
            form = PublicacaoForm()  # Reiniciar o formulário após o sucesso
    else:
        form = PublicacaoForm()
    return render(request, 'publicacao/adicionar_publicacao.html', {'form': form, 'sucesso': sucesso})
