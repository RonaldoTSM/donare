from django.shortcuts import render
from app_criar_perfil_ong.models import CadastroOng
from django.db import IntegrityError

def criar_perfil_ong(request):
    if request.method == 'POST':
        # Lógica para processar os dados do formulário
        print('Dados recebidos no servidor:', request.POST)
        usuario = request.POST.get('nome_de_usuario')
        nome = request.POST.get('nome_completo')
        cnpj = request.POST.get('CPF')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        senha = request.POST.get('passwordInput')

        cpf = ''.join(c for c in cpf if c.isdigit())
        telefone = ''.join(c for c in telefone if c.isdigit())

        novo_usuario = CadastroOng(nome=nome, usuario=usuario, cnpj=cnpj, telefone=telefone, email=email, senha=senha)

        try:
            novo_usuario.save()
            print("Usuário salvo com sucesso.")
        except IntegrityError as e:
            print(f"Erro ao salvar no banco de dados: {e}")

        return render(request, 'cadastro_ong/dados_bancarios.html')
    
    return render(request, 'cadastro_ong/perfil_ong.html')

def dados_bancarios_ong(request):
    return render(request, 'cadastro_ong/dados_bancarios.html')
