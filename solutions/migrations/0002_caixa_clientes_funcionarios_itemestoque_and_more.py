# Generated by Django 4.2.4 on 2023-08-08 12:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("solutions", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Caixa",
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
                ("lucro", models.DecimalField(decimal_places=2, max_digits=10)),
                ("gasto", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="Clientes",
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
                ("nome", models.CharField(max_length=100)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("telefone", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Funcionarios",
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
                ("nome", models.CharField(max_length=100)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("telefone", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="ItemEstoque",
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
                ("codigo", models.PositiveIntegerField(unique=True)),
                ("descricao", models.CharField(max_length=100)),
                ("quantidade", models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name="ferramentas",
            name="codigo",
            field=models.CharField(
                choices=[
                    ("FDC", "Ferramentas de Celular"),
                    ("FDPC", "Ferramentas de Computador"),
                    ("FDN", "Ferramentas de Notebook"),
                ],
                default=(),
                max_length=4,
                unique=True,
            ),
        ),
    ]