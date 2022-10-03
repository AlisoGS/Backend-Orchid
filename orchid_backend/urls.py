from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core import views
from media.router import router as media_router

router = DefaultRouter()
router.register(r"armas", views.ArmaViewSet)
router.register(r"fichas", views.FichaViewSet)
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
    path("api/media/", include(media_router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("api/", include(router.urls)),

]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)