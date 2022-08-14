from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import UsuarioViewSet, OrigemViewSet, PericiaViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'origens', OrigemViewSet)
router.register(r'pericias', PericiaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
