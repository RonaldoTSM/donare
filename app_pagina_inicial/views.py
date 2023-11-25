from django.shortcuts import render, get_object_or_404
from app_criar_perfil_ong.models import CadastroOng
from app_criar_perfil_doador.models import Cadastro
from django.http import HttpResponseRedirect
from django.urls import reverse

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

def edit_ong(request, username):
    ong = get_object_or_404(CadastroOng, username=username)
    return render(request, 'paginas/home_ong.html', {'ong': ong})

def atualizar_infos_ong(request, username):
    if request.method == 'POST':
        ong = get_object_or_404(CadastroOng, username=username)

        # Atualize os campos do modelo com os dados do formulário
        ong.nome = request.POST.get('nome') if request.POST.get('nome') else ong.Nome
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
        ong.interesses = request.POST.get('categoria') if request.POST.get('categoria') else ong.interesses

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