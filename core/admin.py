from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from core.models import (
    Arma,
    Classe,
    Ficha,
    Fichario,
    FicPer,
    Origem,
    Pericia,
    Poder,
    Proficiencia,
    Trilha,
    Usuario,
    Utilitario,
    Vestimenta,
)

admin.site.register(Arma)
admin.site.register(Classe)
admin.site.register(Ficha)
admin.site.register(FicPer)
admin.site.register(Fichario)
admin.site.register(Origem)
admin.site.register(Pericia)
admin.site.register(Poder)
admin.site.register(Proficiencia)
admin.site.register(Trilha)
admin.site.register(Utilitario)
admin.site.register(Vestimenta)



class UsuarioAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "data_nascimento", "foto")}),
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
admin.site.register(Usuario, UsuarioAdmin)