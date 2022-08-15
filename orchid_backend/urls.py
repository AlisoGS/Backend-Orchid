from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core import views

router = DefaultRouter()
router.register(r"atr_fichas", views.AtrFicViewSet)
router.register(r"armas", views.ArmaViewSet)
router.register(r"atributos", views.AtributoViewSet)
router.register(r"fic_pers", views.FicPerViewSet)
router.register(r"fichas", views.FichaViewSet)
router.register(r"origens", views.OrigemViewSet)
router.register(r"pericias", views.PericiaViewSet)
router.register(r"usuarios", views.UsuarioViewSet)
router.register(r"utilitarios", views.UtilitarioViewSet)
router.register(r"vestimentas", views.VestimentaViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
