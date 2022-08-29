# Generated by Django 4.1 on 2022-08-29 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0012_alter_ficper_id_fic_per_alter_ficper_id_per_fic"),
    ]

    operations = [
        migrations.AddField(
            model_name="ficha",
            name="nex",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="ficha",
            name="vida_atu",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="ficha",
            name="vida_max",
            field=models.IntegerField(default=0),
        ),
    ]
