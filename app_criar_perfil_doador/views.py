# Create your views here.
from django.shortcuts import render, redirect
from .models import Usuario  # Corrigido para usar a notação de importação correta

def criar_perfil_doador_interesses(request):
    return render(request, 'cadastro_doador/interesses.html')

def criar_perfil_doador(request):
    if request.method == 'POST':
        # Lógica para processar os dados do formulário
        usuario = request.POST['nome_de_usuario']
        nome = request.POST['nome_completo']
        cpf = request.POST['CPF']
        telefone = request.POST['telefone']
        email = request.POST['email']
        senha = request.POST['passwordInput']

        # Crie uma instância do seu modelo e salve no banco de dados
        usuario = Usuario(username=usuario, nome=nome, cpf=cpf, telefone=telefone, email=email, senha=senha)
        usuario.save()

        # Redirecione para outra página ou faça o que for necessário
        return redirect('criar_perfil_doador_interesses')  # Substitua 'criar_perfil_doador_interesses' pela sua view desejada

    return render(request, 'cadastro_doador/perfil_doador.html')
