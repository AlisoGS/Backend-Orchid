# Generated by Django 4.1.2 on 2022-12-05 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_remove_ficha_pericias_remove_ficper_grau"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ficper",
            name="ficha",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pericias",
                to="core.ficha",
            ),
        ),
    ]