from rest_framework.viewsets import ModelViewSet

from core.models import mod_usuario, mod_origem, mod_pericia
from core.serializers import ser_usuario, ser_origem, ser_pericia

class UsuarioViewSet(ModelViewSet):
    queryset = mod_usuario.Usuario.objects.all()
    serializer_class = ser_usuario.UsuarioSerializer

class OrigemViewSet(ModelViewSet):
    queryset = mod_origem.Origem.objects.all()
    serializer_class = ser_origem.OrigemSerializer

class PericiaViewSet(ModelViewSet):
    queryset = mod_pericia.Pericia.objects.all()
    serializer_class = ser_pericia.PericiaSerializer