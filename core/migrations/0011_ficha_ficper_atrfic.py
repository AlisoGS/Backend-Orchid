# Generated by Django 4.0.6 on 2022-08-15 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_atributo_alter_arma_options_alter_utilitario_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id_ficha', models.AutoField(primary_key=True, serialize=False)),
                ('nome_ficha', models.CharField(max_length=255)),
                ('orig_ficha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='fichas', to='core.origem')),
                ('user_ficha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='fichas', to='core.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='FicPer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grau_pericia', models.IntegerField(choices=[(1, 'D'), (2, 'T'), (3, 'V'), (4, 'E')])),
                ('id_fic_per', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='FicPers', to='core.ficha')),
                ('id_per_fic', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='PerFics', to='core.pericia')),
            ],
        ),
        migrations.CreateModel(
            name='AtrFic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField(default=1)),
                ('id_atr_fic', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='atr_fic', to='core.atributo')),
                ('id_fic_atr', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='atr_fic', to='core.ficha')),
            ],
        ),
    ]
