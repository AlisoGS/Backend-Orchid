from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core import views

router = DefaultRouter()
router.register(r"armas", views.ArmaViewSet)
router.register(r"origens", views.OrigemViewSet)
router.register(r"pericias", views.PericiaViewSet)
router.register(r"usuarios", views.UsuarioViewSet)
router.register(r"utilitarios", views.UtilitarioViewSet)
router.register(r"vestimenta", views.VestimentaViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
