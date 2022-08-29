from rest_framework.viewsets import ModelViewSet
from core.models import usuario
from core.serializers.usuario import UsuarioSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = usuario.Usuario.objects.all()
    serializer_class = UsuarioSerializer
