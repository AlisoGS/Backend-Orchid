from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

from core import views


router = DefaultRouter()
router.register(r"armas", views.ArmaViewSet)
router.register(r"atributos", views.AtributoViewSet)
router.register(r"fichas", views.FichaViewSet)
router.register(r"ficha-atributos", views.FicAtrViewSet)
router.register(r"ficha-pericias", views.FicPerViewSet)
router.register(r"origens", views.OrigemViewSet)
router.register(r"pericias", views.PericiaViewSet)
router.register(r"poderes", views.PoderViewSet)
router.register(r"proficiencias", views.ProficienciaViewSet)
router.register(r"trilha", views.TrilhaViewSet)
router.register(r"usuarios", views.UsuarioViewSet)
router.register(r"utilitarios", views.UtilitarioViewSet)
router.register(r"vestimentas", views.VestimentaViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
