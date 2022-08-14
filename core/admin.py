from django.contrib import admin

from core.models import mod_usuario, mod_origem, mod_pericia

admin.site.register(mod_usuario.Usuario)
admin.site.register(mod_origem.Origem)
admin.site.register(mod_pericia.Pericia)
