# Generated by Django 5.0.6 on 2024-07-05 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_cor"),
    ]

    operations = [
        migrations.CreateModel(
            name="Marca",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=50)),
                ("nacionalidade", models.CharField(max_length=50)),
            ],
            options={
                "verbose_name": "Marca",
                "verbose_name_plural": "Marcas",
            },
        ),
        migrations.AlterModelOptions(
            name="cor",
            options={"verbose_name": "Cor", "verbose_name_plural": "Cores"},
        ),
    ]
