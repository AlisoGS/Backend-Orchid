from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import atributo, ficha, item, origem, pericia, usuario, proficiencia

router = DefaultRouter()
router.register(r"armas", item.ArmaViewSet)
router.register(r"atributos", atributo.AtributoViewSet)
router.register(r"ficha_pericias", ficha.FicPerViewSet)
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
