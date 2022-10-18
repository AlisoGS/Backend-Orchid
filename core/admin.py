from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from core import models

admin.site.register(models.Arma)
admin.site.register(models.Classe)
admin.site.register(models.Ficha)
admin.site.register(models.FicPer)
admin.site.register(models.Fichario)
admin.site.register(models.Origem)
admin.site.register(models.Pericia)
admin.site.register(models.Poder)
admin.site.register(models.Proficiencia)
admin.site.register(models.Trilha)
admin.site.register(models.Utilitario)
admin.site.register(models.Vestimenta)


class UsuarioAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "data_nascimento")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
admin.site.register(models.Usuario, UsuarioAdmin)