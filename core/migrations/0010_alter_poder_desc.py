# Generated by Django 4.1.1 on 2022-10-13 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0009_alter_ficha_poderes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="poder",
            name="desc",
            field=models.TextField(max_length=600),
        ),
    ]
