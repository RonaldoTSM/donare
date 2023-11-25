"""
URL configuration for projeto_donare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_tela_inicial import views
from app_criar_perfil_doador import views as criar_doador_views
from app_criar_perfil_ong import views as criar_ong_views
from app_login import views as login_views
from app_pagina_inicial import views as home_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.tela_inicial, name='tela_inicial'),
    path('cadastro_doador/perfil_doador', criar_doador_views.criar_perfil_doador, name='criar_perfil_doador'),
    path('cadastro_doador/perfil_doador/interesses/', criar_doador_views.salvar_interesses, name='criar_perfil_doador_interesses'),
    path('cadastro_ong/perfil_ong', criar_ong_views.criar_perfil_ong, name='perfil_ong'),
    path('cadastro_ong/dados_bancarios/', criar_ong_views.dados_bancarios_ong, name='dados_bancarios_ong'),
    path('login/', login_views.login, name='login'),    
    path('doador/<str:username>/', home_views.home_doador, name='home_doador'),    
    path('ong/<str:username>/', home_views.home_ong, name='home_ong'),
    path('doador/<str:username>/edit', home_views.edit_doador, name="editar_infos_doador"),    
    path('doador/adicionar_publicacao/', home_views.adicionar_publicacao, name='adicionar_publicacao'),
    ]
