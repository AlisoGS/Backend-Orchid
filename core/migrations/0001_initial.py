# Generated by Django 4.0.6 on 2022-08-01 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('nome_user', models.CharField(max_length=255)),
            ],
        ),
    ]
