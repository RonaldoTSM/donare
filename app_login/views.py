from django.shortcuts import render, redirect
from app_criar_perfil_ong.models import CadastroOng
from app_criar_perfil_doador.models import Cadastro
from django.urls import reverse

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['senha']
        try:
            user_ong = CadastroOng.objects.get(username=username)
            if user_ong.senha == senha:
                return redirect(reverse('home_ong', kwargs={'username': username}))  
            else:
                return render(request, 'login/login.html', {'error': 'Senha incorreta.'})
        except CadastroOng.DoesNotExist:
            try:
                user_doador = Cadastro.objects.get(username=username)
                if user_doador.senha == senha:
                    return redirect(reverse('home_doador', kwargs={'username': username}))  
                else:
                    return render(request, 'login/login.html', {'error': 'Senha incorreta.'})
            except Cadastro.DoesNotExist:
                return render(request, 'login/login.html', {'error': 'Usuário não encontrado.'})
    return render(request, 'login/login.html')
