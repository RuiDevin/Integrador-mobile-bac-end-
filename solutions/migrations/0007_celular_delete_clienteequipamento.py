# Generated by Django 4.2.4 on 2023-08-22 18:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("solutions", "0006_alter_clienteequipamento_celular_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Celular",
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
                ("modelo", models.CharField(max_length=100)),
                ("diagnostico", models.CharField(max_length=100)),
                ("data_entrada", models.DateField()),
                (
                    "codigo_progresso",
                    models.UUIDField(default=uuid.uuid4, editable=False),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="ClienteEquipamento",
        ),
    ]
