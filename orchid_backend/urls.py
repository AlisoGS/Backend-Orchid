from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import atr_fic, atributo, fic_per, ficha, item, origem, pericia, usuario, proficiencia

router = DefaultRouter()
router.register(r"atr_fichas", atr_fic.AtrFicViewSet)
router.register(r"armas", item.ArmaViewSet)
router.register(r"atributos", atributo.AtributoViewSet)
router.register(r"fic_pers", fic_per.FicPerViewSet)
router.register(r"fichas", ficha.FichaViewSet)
router.register(r"origens", origem.OrigemViewSet)
router.register(r"pericias", pericia.PericiaViewSet)
router.register(r"proficiencias", proficiencia.ProficienciaViewSet)
router.register(r"usuarios", usuario.UsuarioViewSet)
router.register(r"utilitarios", item.UtilitarioViewSet)
router.register(r"vestimentas", item.VestimentaViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
