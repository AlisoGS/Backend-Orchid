from rest_framework.viewsets import ModelViewSet
from core.models import mod_usuario
from core.serializers import ser_usuario

class UsuarioViewSet(ModelViewSet):
    queryset = mod_usuario.Usuario.objects.all()
    serializer_class = ser_usuario.UsuarioSerializer
