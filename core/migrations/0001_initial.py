# Generated by Django 4.1.1 on 2022-10-03 14:26

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("media", "0001_initial"),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Usuario",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "data_nascimento",
                    models.DateField(blank=True, default=None, null=True),
                ),
                (
                    "foto",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="media.image",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Arma",
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
                ("nome", models.CharField(max_length=255)),
                ("desc", models.CharField(blank=True, max_length=400, null=True)),
                ("espaco", models.IntegerField(default=1)),
                ("num_dados", models.IntegerField(default=None)),
                ("tipo_dado", models.IntegerField(default=None)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Ficha",
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
                ("nome", models.CharField(max_length=255)),
                ("nex", models.PositiveIntegerField(default=0)),
                ("vida_max", models.IntegerField(default=0)),
                ("vida_atu", models.IntegerField(default=0)),
                ("sani_max", models.IntegerField(default=0)),
                ("sani_atu", models.IntegerField(default=0)),
                ("agili", models.SmallIntegerField(default=0)),
                ("forca", models.SmallIntegerField(default=0)),
                ("intel", models.SmallIntegerField(default=0)),
                ("prese", models.SmallIntegerField(default=0)),
                ("vigor", models.SmallIntegerField(default=0)),
                (
                    "foto",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="media.image",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Pericia",
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
                ("nome", models.CharField(max_length=40)),
                ("desc", models.TextField(max_length=255)),
                ("penalidade_carga", models.BooleanField(default=False)),
                ("somente_treinado", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Poder",
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
                ("nome", models.CharField(max_length=40)),
                ("desc", models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Proficiencia",
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
                ("nome", models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name="Trilha",
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
                ("nome", models.CharField(max_length=40)),
                ("desc", models.TextField(max_length=255)),
                ("nomeNex10", models.TextField(default=None, max_length=70)),
                ("descNex10", models.TextField(default=None, max_length=600)),
                ("nomeNex30", models.TextField(default=None, max_length=70)),
                ("descNex30", models.TextField(default=None, max_length=600)),
                ("nomeNex65", models.TextField(default=None, max_length=70)),
                ("descNex65", models.TextField(default=None, max_length=600)),
                ("nomeNex99", models.TextField(default=None, max_length=70)),
                ("descNex99", models.TextField(default=None, max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name="Utilitario",
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
                ("nome", models.CharField(max_length=255)),
                ("desc", models.CharField(blank=True, max_length=400, null=True)),
                ("espaco", models.IntegerField(default=1)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Vestimenta",
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
                ("nome", models.CharField(max_length=255)),
                ("desc", models.CharField(blank=True, max_length=400, null=True)),
                ("espaco", models.IntegerField(default=1)),
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
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(default=None, max_length=50)),
                ("desc", models.TextField(default=None, max_length=1000)),
                ("poder", models.TextField(default=None, max_length=400)),
                (
                    "pericia1",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="core.pericia",
                    ),
                ),
                (
                    "pericia2",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
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
                    "grau",
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
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="FicPer",
                        to="core.ficha",
                    ),
                ),
                (
                    "pericia",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
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
            name="orig",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
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
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="fichas",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
