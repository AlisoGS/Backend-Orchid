from django.contrib import admin

from core.models import usuario, origem, pericia, item, atributo, ficha, atr_fic, fic_per, proficiencia

admin.site.register(usuario.Usuario)
admin.site.register(origem.Origem)
admin.site.register(pericia.Pericia)
admin.site.register(item.Arma)
admin.site.register(item.Utilitario)
admin.site.register(item.Vestimenta)
admin.site.register(atributo.Atributo)
admin.site.register(ficha.Ficha)
admin.site.register(atr_fic.AtrFic)
admin.site.register(fic_per.FicPer)
admin.site.register(proficiencia.Proficiencia)
