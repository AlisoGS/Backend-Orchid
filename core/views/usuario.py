from rest_framework.viewsets import ModelViewSet
from core.models import usuario
from core.serializers import ser_usuario

class UsuarioViewSet(ModelViewSet):
    queryset = usuario.Usuario.objects.all()
    serializer_class = ser_usuario.UsuarioSerializer
