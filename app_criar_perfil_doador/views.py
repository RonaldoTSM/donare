from app_criar_perfil_doador.models import Cadastro
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.http import JsonResponse

def criar_perfil_doador_interesses(request):
    return render(request, 'cadastro_doador/interesses.html')

def criar_perfil_doador(request):
    if request.method == 'POST':
        # Lógica para processar os dados do formulário
        print('Dados recebidos no servidor:', request.POST)
        username = request.POST.get('nome_de_usuario')
        Nome = request.POST.get('nome_completo')
        cpf = request.POST.get('CPF')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        senha = request.POST.get('passwordInput')
        nascimento = request.POST.get('Nascimento')
        descricao = request.POST.get('descricao')
        cep = request.POST.get('CEP')
        rua = request.POST.get('Rua')
        numero = request.POST.get('numero')
        complemento = request.POST.get('complemento')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')

        cpf = ''.join(c for c in cpf if c.isdigit())
        telefone = ''.join(c for c in telefone if c.isdigit())
        nascimento = ''.join(c for c in nascimento if c.isdigit())
        cep = ''.join(c for c in cep if c.isdigit())

        # Crie uma instância do seu modelo e salve no banco de dados
        novo_usuario = Cadastro(Nome=Nome, username=username, senha=senha, cpf=cpf, email=email, telefone=telefone, nascimento=nascimento, descricao=descricao, rua=rua, numero=numero, complemento=complemento, bairro=bairro, cidade=cidade, estado=estado, cep=cep)
        try:
            novo_usuario.save()
            print("Usuário salvo com sucesso.")
            return JsonResponse({'success': True})
        except IntegrityError as e:
            if 'UNIQUE constraint failed' in str(e):
                error_message = "Os dados já existem. Por favor, verifique e tente novamente."
            else:
                error_message = f"Erro ao cadastrar usuário"
            print(error_message)
            return JsonResponse({'success': False, 'error_message': error_message})

    return render(request, 'cadastro_doador/perfil_doador.html')