from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny

from core.models import Usuario
from core.serializers import UsuarioDetailSerializer, UsuarioSerializer


class UsuarioViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return UsuarioDetailSerializer
        return UsuarioSerializer

    def get_queryset(self):
        usuario = self.request.user
        return Usuario.objects.filter(id=usuario.id)

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]
        return [IsAuthenticated()]
