from rest_framework.viewsets import ModelViewSet

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
