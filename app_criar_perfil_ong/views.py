from django.shortcuts import render
from app_criar_perfil_ong.models import CadastroOng
from django.db import IntegrityError

def criar_perfil_ong(request):
    if request.method == 'POST':
        # Lógica para processar os dados do formulário
        print('Dados recebidos no servidor:', request.POST)
        username = request.POST.get('nome_de_usuario')
        nome = request.POST.get('nome_completo')
        cnpj = request.POST.get('cnpj')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        senha = request.POST.get('passwordInput')

        cnpj = ''.join(c for c in cnpj if c.isdigit())
        telefone = ''.join(c for c in telefone if c.isdigit())

        novo_usuario = CadastroOng(nome=nome, username=username, cnpj=cnpj, telefone=telefone, email=email, senha=senha)

        try:
            novo_usuario.save()
            print("Usuário salvo com sucesso.")
        except IntegrityError as e:
            print(f"Erro ao salvar no banco de dados: {e}")

        return render(request, 'cadastro_ong/dados_bancarios.html')
    
    return render(request, 'cadastro_ong/perfil_ong.html')

def dados_bancarios_ong(request):
    return render(request, 'cadastro_ong/dados_bancarios.html')
