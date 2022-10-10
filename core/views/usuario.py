from rest_framework.viewsets import ModelViewSet

from core.models import Usuario
from core.serializers import UsuarioDetailSerializer, UsuarioSerializer


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()


    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return UsuarioDetailSerializer
        return UsuarioSerializer
