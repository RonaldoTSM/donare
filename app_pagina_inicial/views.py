from django.shortcuts import render

def home_doador(request):
    return render(request, 'paginas/home_doador.html')

def home_ong(request):
    return render(request, 'paginas/home_ong.html')
