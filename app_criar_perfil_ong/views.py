from django.shortcuts import render
from app_criar_perfil_ong.models import CadastroOng, DadosBancariosOng
from django.db import IntegrityError
from django.http import JsonResponse
import json

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
        categoria = request.POST.get('categoria')
        descricao = request.POST.get('descricao')
        cep = request.POST.get('cep')
        rua = request.POST.get('rua')
        numero = request.POST.get('numero')
        complemento = request.POST.get('complemento')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')

        cnpj = ''.join(c for c in cnpj if c.isdigit())
        telefone = ''.join(c for c in telefone if c.isdigit())

        novo_usuario = CadastroOng(nome=nome, username=username, cnpj=cnpj, telefone=telefone, email=email, senha=senha, categoria=categoria, descricao=descricao, cep=cep, rua=rua, numero=numero, complemento=complemento, bairro=bairro, cidade=cidade, estado=estado)

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

    return render(request, 'cadastro_ong/perfil_ong.html')

def dados_bancarios_ong(request):
    if request.method == 'POST':
        print('Dados recebidos no servidor')
        data = json.loads(request.body)
        ong_user = data.get('username')
        nome_titular = data.get('nome_titular')
        conta = data.get('conta')
        agencia = data.get('agencia')
        banco = data.get('banco')
        tipoConta = data.get('tipoConta')
        cidade = data.get('cidade')
        estado = data.get('estado')
        pix = data.get('pix')
        obs = data.get('obs')

        dados_bancarios = DadosBancariosOng(
            ong_user=ong_user, 
            nome_titular=nome_titular, 
            conta=conta, 
            agencia=agencia, 
            banco=banco, 
            tipoConta=tipoConta, 
            cidade=cidade, 
            estado=estado, 
            pix=pix, 
            obs=obs
        )

        try:
            dados_bancarios.save()
            print("Dados salvos com sucesso.")
            return JsonResponse({'success': True})
        except Exception as e:
            print(f"Erro ao salvar dados: {e}")

    return render(request, 'cadastro_ong/dados_bancarios.html')
