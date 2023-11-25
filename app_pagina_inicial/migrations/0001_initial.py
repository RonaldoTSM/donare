# Generated by Django 4.2.4 on 2023-11-25 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("app_criar_perfil_doador", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Publicacao",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=200)),
                ("descricao", models.TextField()),
                ("data_publicacao", models.DateTimeField(auto_now_add=True)),
                (
                    "autor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="publicacoes",
                        to="app_criar_perfil_doador.cadastro",
                    ),
                ),
            ],
            options={
                "db_table": "publicacoes",
            },
        ),
    ]
