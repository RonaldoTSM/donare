# Generated by Django 4.2.5 on 2023-11-24 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroOng',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('cnpj', models.CharField(max_length=20, unique=True)),
                ('telefone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('senha', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=500)),
                ('cep', models.CharField(max_length=9)),
                ('rua', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=10)),
                ('complemento', models.CharField(max_length=20)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'dados-cadastrais-ong',
            },
        ),
        migrations.CreateModel(
            name='DadosBancariosOng',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ong_user', models.CharField(max_length=50)),
                ('nome_titular', models.CharField(max_length=50)),
                ('conta', models.CharField(max_length=50)),
                ('agencia', models.CharField(max_length=50)),
                ('banco', models.CharField(max_length=50)),
                ('tipoConta', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('pix', models.CharField(max_length=50)),
                ('obs', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'ong-dados-bancarios',
            },
        ),
    ]
