# Generated by Django 4.1 on 2022-09-08 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Arma",
            fields=[
                ("id_item", models.AutoField(primary_key=True, serialize=False)),
                ("nome_item", models.CharField(max_length=255)),
                ("desc_item", models.CharField(blank=True, max_length=400, null=True)),
                ("espaco_item", models.IntegerField(default=1)),
                ("num_dados", models.IntegerField(default=None)),
                ("tipo_dado", models.IntegerField(default=None)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Atributo",
            fields=[
                ("id_atributo", models.AutoField(primary_key=True, serialize=False)),
                ("nome_atributo", models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name="FicAtr",
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
                ("valor", models.SmallIntegerField()),
                (
                    "atributo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="FicAtr",
                        to="core.atributo",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "FichaAtributos",
            },
        ),
        migrations.CreateModel(
            name="Ficha",
            fields=[
                ("id_ficha", models.AutoField(primary_key=True, serialize=False)),
                ("nome_ficha", models.CharField(max_length=255)),
                ("nex", models.PositiveIntegerField(default=0)),
                ("vida_max", models.IntegerField(default=0)),
                ("vida_atu", models.IntegerField(default=0)),
                ("sani_max", models.IntegerField(default=0)),
                ("sani_atu", models.IntegerField(default=0)),
                (
                    "atributos",
                    models.ManyToManyField(
                        related_name="fichas", through="core.FicAtr", to="core.atributo"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Pericia",
            fields=[
                ("id_pericia", models.AutoField(primary_key=True, serialize=False)),
                ("nome_pericia", models.CharField(max_length=40)),
                ("desc_pericia", models.TextField(max_length=255)),
                ("penalidade_carga", models.BooleanField(default=False)),
                ("somente_treinado", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Proficiencia",
            fields=[
                (
                    "id_proficiancia",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("nome_proficiencia", models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name="Usuario",
            fields=[
                ("id_user", models.AutoField(primary_key=True, serialize=False)),
                (
                    "login_user",
                    models.CharField(default=None, max_length=255, unique=True),
                ),
                ("nome_user", models.CharField(default=None, max_length=255)),
                ("sobrenome_user", models.CharField(default=None, max_length=255)),
                (
                    "email_user",
                    models.EmailField(default=None, max_length=255, unique=True),
                ),
                ("password_user", models.CharField(default=None, max_length=255)),
                ("active_user", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Utilitario",
            fields=[
                ("id_item", models.AutoField(primary_key=True, serialize=False)),
                ("nome_item", models.CharField(max_length=255)),
                ("desc_item", models.CharField(blank=True, max_length=400, null=True)),
                ("espaco_item", models.IntegerField(default=1)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Vestimenta",
            fields=[
                ("id_item", models.AutoField(primary_key=True, serialize=False)),
                ("nome_item", models.CharField(max_length=255)),
                ("desc_item", models.CharField(blank=True, max_length=400, null=True)),
                ("espaco_item", models.IntegerField(default=1)),
                ("modificador_esq", models.IntegerField(default=None)),
                ("modificador_pas", models.IntegerField(default=None)),
                ("modificador_blo", models.IntegerField(default=None)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Origem",
            fields=[
                ("id_origem", models.AutoField(primary_key=True, serialize=False)),
                ("nome_origem", models.CharField(default=None, max_length=50)),
                ("desc_origem", models.TextField(default=None, max_length=1000)),
                ("poder_origem", models.TextField(default=None, max_length=400)),
                (
                    "pericia1",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="core.pericia",
                    ),
                ),
                (
                    "pericia2",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="core.pericia",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Origens",
            },
        ),
        migrations.CreateModel(
            name="FicPer",
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
                (
                    "grau_pericia",
                    models.IntegerField(
                        choices=[
                            (1, "Destreinado"),
                            (2, "Treinado"),
                            (3, "Veterano"),
                            (4, "Expert"),
                        ],
                        default=1,
                    ),
                ),
                (
                    "ficha",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="FicPer",
                        to="core.ficha",
                    ),
                ),
                (
                    "pericia",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="PerFic",
                        to="core.pericia",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "FichaPericias",
                "unique_together": {("ficha", "pericia")},
            },
        ),
        migrations.AddField(
            model_name="ficha",
            name="orig_ficha",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="fichas",
                to="core.origem",
            ),
        ),
        migrations.AddField(
            model_name="ficha",
            name="pericias",
            field=models.ManyToManyField(
                related_name="fichas", through="core.FicPer", to="core.pericia"
            ),
        ),
        migrations.AddField(
            model_name="ficha",
            name="user_ficha",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="fichas",
                to="core.usuario",
            ),
        ),
        migrations.AddField(
            model_name="ficatr",
            name="ficha",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="FicAtr",
                to="core.ficha",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="ficatr",
            unique_together={("ficha", "atributo")},
        ),
    ]
