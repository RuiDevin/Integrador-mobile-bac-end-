# Generated by Django 4.2.4 on 2023-08-22 19:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("solutions", "0007_celular_delete_clienteequipamento"),
    ]

    operations = [
        migrations.CreateModel(
            name="Desktop",
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
                ("data_entrada", models.DateField()),
                ("motivo_entrada", models.CharField(max_length=100)),
                (
                    "codigo_progresso",
                    models.UUIDField(default=uuid.uuid4, editable=False),
                ),
            ],
        ),
    ]
