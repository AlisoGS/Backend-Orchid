# Generated by Django 4.1.1 on 2022-10-10 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_alter_poder_options_arma_ficha_utilitario_ficha_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="ficper",
            options={"verbose_name_plural": "fichapericias"},
        ),
        migrations.AlterModelOptions(
            name="origem",
            options={"verbose_name_plural": "origens"},
        ),
        migrations.AlterModelOptions(
            name="poder",
            options={"verbose_name_plural": "poderes"},
        ),
    ]