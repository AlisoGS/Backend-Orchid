from rest_framework.viewsets import ModelViewSet
from core.models import usuario
from core.serializers.usuario import UsuarioSerializer
from rest_framework.permissions import IsAuthenticated


class UsuarioViewSet(ModelViewSet):
    queryset = usuario.Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]