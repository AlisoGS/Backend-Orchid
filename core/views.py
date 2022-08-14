from rest_framework.viewsets import ModelViewSet

from core.models import mod_usuario, mod_origem, mod_pericia, mod_item
from core.serializers import ser_usuario, ser_origem, ser_pericia, ser_item

class UsuarioViewSet(ModelViewSet):
    queryset = mod_usuario.Usuario.objects.all()
    serializer_class = ser_usuario.UsuarioSerializer

class OrigemViewSet(ModelViewSet):
    queryset = mod_origem.Origem.objects.all()
    serializer_class = ser_origem.OrigemSerializer

class PericiaViewSet(ModelViewSet):
    queryset = mod_pericia.Pericia.objects.all()
    serializer_class = ser_pericia.PericiaSerializer

class ArmaViewSet(ModelViewSet):
    queryset = mod_item.Arma.objects.all()
    serializer_class = ser_item.ArmaSerializer

class UtilitarioViewSet(ModelViewSet):
    queryset = mod_item.Utilitario.objects.all()
    serializer_class = ser_item.UtilitarioSerializer

class VestimentaViewSet(ModelViewSet):
    queryset = mod_item.Vestimenta.objects.all()
    serializer_class = ser_item.VestimentaSerializer