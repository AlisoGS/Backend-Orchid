from django.contrib import admin

from core.models import mod_usuario, mod_origem, mod_pericia, mod_item, mod_atributo, mod_ficha, mod_atr_fic, mod_fic_per

admin.site.register(mod_usuario.Usuario)
admin.site.register(mod_origem.Origem)
admin.site.register(mod_pericia.Pericia)
admin.site.register(mod_item.Arma)
admin.site.register(mod_item.Utilitario)
admin.site.register(mod_item.Vestimenta)
admin.site.register(mod_atributo.Atributo)
admin.site.register(mod_ficha.Ficha)
admin.site.register(mod_atr_fic.AtrFic)
admin.site.register(mod_fic_per.FicPer)
