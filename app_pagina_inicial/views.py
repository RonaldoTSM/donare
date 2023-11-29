from django.shortcuts import render, get_object_or_404, redirect
from app_criar_perfil_ong.models import CadastroOng
from app_criar_perfil_doador.models import Cadastro
from app_criar_perfil_ong.models import DadosBancariosOng
from .models import Doacoes
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import PublicacaoForm, DoacaoForm
from .models import Publicacao
from django.db.models import Q
from django.http import JsonResponse



def home_ong(request, username):
    ong = get_object_or_404(CadastroOng, username=username)
    doacoes = Doacoes.objects.filter(
        Q(ong=ong)
    ).order_by('-data_publicacao')
    return render(request, 'paginas/home_ong.html', {'ong': ong, 'doacoes': doacoes})

def home_doador(request, username):
    doador = get_object_or_404(Cadastro, username=username)
    publicacoes = Publicacao.objects.all().order_by('-data_publicacao') 
    ongs = CadastroOng.objects.all()
    interesses_usuario = doador.interesses.split(',')
    doacoes = Doacoes.objects.filter(
        Q(autor=doador)
    ).order_by('-data_publicacao')
    
    ongs_interesses = CadastroOng.objects.filter(
        Q(categoria__in=interesses_usuario)
    )
    dadosBancarios = DadosBancariosOng.objects.all()

    doador.nascimento = formatar_data_nascimento(doador.nascimento)
    doador.telefone = formatar_telefone(doador.telefone)

    return render(request, 'paginas/home_doador.html', {'doador': doador, 'publicacoes': publicacoes, 'ongs': ongs, 'ongs_interesses': ongs_interesses, 'dadosBancarios': dadosBancarios, 'doacoes': doacoes})

def getDadosBancarios(request, ongUser):

    try:
        dadosBancarios = DadosBancariosOng.objects.get(ong_user=ongUser)

        response_data = {
            "ong_user": dadosBancarios.ong_user,
            "nome_titular": dadosBancarios.nome_titular,
            "conta": dadosBancarios.conta,
            "agencia": dadosBancarios.agencia,
            "banco": dadosBancarios.banco,
            "tipoConta": dadosBancarios.tipoConta,
            "pix": dadosBancarios.pix,
            "obs": dadosBancarios.obs
        }

        return JsonResponse(response_data)
    
    except DadosBancariosOng.DoesNotExist:
        # Trate o caso em que não há dados bancários para o usuário da ONG
        return JsonResponse({'error': 'Dados bancários não encontrados'}, status=404)

def edit_doador(request, username):
    doador = Cadastro.objects.get(username=username)    
    return render(request, 'paginas/home_doador_edit.html', {'doador': doador})

def save_doacao(request, username, user_ong):
    ong = get_object_or_404(CadastroOng, username=user_ong)
    doador = get_object_or_404(Cadastro, username=username)

    if request.method == 'POST':
        # Altere para usar request.POST diretamente
        forma_pagamento = request.POST.get('forma_pagamento')
        valor = request.POST.get('valor')

        # Crie um dicionário com os dados do formulário
        form_data = {
            'forma_pagamento': forma_pagamento,
            'valor': valor,
        }

        form = DoacaoForm(form_data)  # Use your donation form here
        if form.is_valid():
            # Create and save the donation
            doacao = form.save(commit=False)
            doacao.ong = ong
            doacao.autor = doador
            doacao.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        # Handle GET requests or other HTTP methods if needed
        return JsonResponse({'success': False, 'errors': 'Invalid request method'})

def adicionar_publicacao(request, username):
    usuario = get_object_or_404(CadastroOng, username=username)

    if request.method == 'POST':
        form = PublicacaoForm(request.POST)
        if form.is_valid():
            publicacao = form.save(commit=False)
            publicacao.autor = usuario
            publicacao.save()

            messages.success(request, "Publicação criada com sucesso!")
            return HttpResponseRedirect(reverse('home_ong', kwargs={'username': username}))  
    
    else:
        form = PublicacaoForm()

    return render(request, 'template_adicionar_publicacao.html', {'form': form, 'usuario': usuario})
    
def edit_ong(request, username):
    ong = get_object_or_404(CadastroOng, username=username)
    return render(request, 'paginas/home_ong_edit.html', {'ong': ong})

def edit_banco(request, username):
    dadosBancarios = get_object_or_404(DadosBancariosOng, ong_user=username)
    return render(request, 'paginas/home_ong_edit_banco.html', {'dadosBancarios': dadosBancarios})

def atualizar_infos_banco(request, username):
    if request.method == 'POST':
        dadosBancarios = get_object_or_404(DadosBancariosOng, ong_user=username)

        dadosBancarios.nome_titular = request.POST.get('nome_titular') if request.POST.get('nome_titular') else dadosBancarios.nome_titular
        dadosBancarios.conta = request.POST.get('conta') if request.POST.get('conta') else dadosBancarios.conta
        dadosBancarios.agencia = request.POST.get('agencia') if request.POST.get('agencia') else dadosBancarios.agencia
        dadosBancarios.banco = request.POST.get('banco') if request.POST.get('banco') else dadosBancarios.banco
        dadosBancarios.tipoConta = request.POST.get('tipoConta') if request.POST.get('tipoConta') else dadosBancarios.tipoConta
        dadosBancarios.cidade = request.POST.get('cidade') if request.POST.get('cidade') else dadosBancarios.cidade
        dadosBancarios.estado = request.POST.get('estado') if request.POST.get('estado') else dadosBancarios.estado
        dadosBancarios.pix = request.POST.get('pix') if request.POST.get('pix') else dadosBancarios.pix
        dadosBancarios.obs = request.POST.get('obs') if request.POST.get('obs') else dadosBancarios.obs

        if any([request.POST.get(field) for field in ['nome_titular', 'conta', 'agencia', 'banco', 'tipoConta', 'cidade', 'estado', 'pix', 'obs']]):
            dadosBancarios.save()

        # Redirecione para a página de visualização do perfil do doador
        return HttpResponseRedirect(reverse('home_ong', args=[username]))

    # Se a requisição não for POST, apenas redirecione para a página de visualização do perfil do doador
    return HttpResponseRedirect(reverse('home_ongr', args=[username]))

def atualizar_infos_ong(request, username):
    if request.method == 'POST':
        ong = get_object_or_404(CadastroOng, username=username)

        # Atualize os campos do modelo com os dados do formulário
        ong.nome = request.POST.get('nome') if request.POST.get('nome') else ong.nome
        ong.senha = request.POST.get('senha') if request.POST.get('senha') else ong.senha
        ong.email = request.POST.get('email') if request.POST.get('email') else ong.email
        ong.telefone = request.POST.get('telefone') if request.POST.get('telefone') else ong.telefone
        ong.descricao = request.POST.get('descricao') if request.POST.get('descricao') else ong.descricao
        ong.rua = request.POST.get('rua') if request.POST.get('rua') else ong.rua
        ong.numero = request.POST.get('numero') if request.POST.get('numero') else ong.numero
        ong.complemento = request.POST.get('complemento') if request.POST.get('complemento') else ong.complemento
        ong.bairro = request.POST.get('bairro') if request.POST.get('bairro') else ong.bairro
        ong.cidade = request.POST.get('cidade') if request.POST.get('cidade') else ong.cidade
        ong.estado = request.POST.get('estado') if request.POST.get('estado') else ong.estado
        ong.cep = request.POST.get('cep') if request.POST.get('cep') else ong.cep
        ong.categoria = request.POST.get('categoria') if request.POST.get('categoria') else ong.categoria

        # Salve as alterações apenas se pelo menos um campo foi atualizado
        if any([request.POST.get(field) for field in ['nome', 'usuario', 'senha', 'email', 'telefone', 'nascimento', 'descricao', 'rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'cep', 'categoria']]):
            ong.save()

        # Redirecione para a página de visualização do perfil do doador
        return HttpResponseRedirect(reverse('home_ong', args=[username]))

    # Se a requisição não for POST, apenas redirecione para a página de visualização do perfil do doador
    return HttpResponseRedirect(reverse('home_ongr', args=[username]))

def atualizar_infos_doador(request, username):
    if request.method == 'POST':
        doador = get_object_or_404(Cadastro, username=username)

        # Atualize os campos do modelo com os dados do formulário
        doador.Nome = request.POST.get('nome') if request.POST.get('nome') else doador.Nome
        doador.senha = request.POST.get('senha') if request.POST.get('senha') else doador.senha
        doador.email = request.POST.get('email') if request.POST.get('email') else doador.email
        doador.telefone = request.POST.get('telefone') if request.POST.get('telefone') else doador.telefone
        doador.descricao = request.POST.get('descricao') if request.POST.get('descricao') else doador.descricao
        doador.rua = request.POST.get('rua') if request.POST.get('rua') else doador.rua
        doador.numero = request.POST.get('numero') if request.POST.get('numero') else doador.numero
        doador.complemento = request.POST.get('complemento') if request.POST.get('complemento') else doador.complemento
        doador.bairro = request.POST.get('bairro') if request.POST.get('bairro') else doador.bairro
        doador.cidade = request.POST.get('cidade') if request.POST.get('cidade') else doador.cidade
        doador.estado = request.POST.get('estado') if request.POST.get('estado') else doador.estado
        doador.cep = request.POST.get('cep') if request.POST.get('cep') else doador.cep
        doador.interesses = request.POST.get('interesses') if request.POST.get('interesses') else doador.interesses

        # Salve as alterações apenas se pelo menos um campo foi atualizado
        if any([request.POST.get(field) for field in ['nome', 'usuario', 'senha', 'email', 'telefone', 'nascimento', 'descricao', 'rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'cep', 'interesses']]):
            doador.save()

        # Redirecione para a página de visualização do perfil do doador
        return HttpResponseRedirect(reverse('home_doador', args=[username]))

    # Se a requisição não for POST, apenas redirecione para a página de visualização do perfil do doador
    return HttpResponseRedirect(reverse('home_doador', args=[username]))

def formatar_data_nascimento(nascimento):
    # Supondo que nascimento seja uma string no formato 'YYYYMMDD'
    return f'{nascimento[6:8]}/{nascimento[4:6]}/{nascimento[:4]}' if len(nascimento) == 8 else nascimento

def formatar_telefone(telefone):
    # Supondo que telefone seja uma string de 11 dígitos
    return f'({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}' if len(telefone) == 11 else telefone
