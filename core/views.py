from rest_framework.viewsets import ModelViewSet

from core.models import mod_usuario, mod_origem, mod_pericia, mod_item, mod_atributo, mod_ficha, mod_fic_per, mod_atr_fic
from core.serializers import ser_usuario, ser_origem, ser_pericia, ser_item, ser_atributo, ser_ficha, ser_fic_per, ser_atr_fic

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

class AtributoViewSet(ModelViewSet):
    queryset = mod_atributo.Atributo.objects.all()
    serializer_class = ser_atributo.AtributoSerializer

class FichaViewSet(ModelViewSet):
    queryset = mod_ficha.Ficha.objects.all()
    serializer_class = ser_ficha.FichaSerializer

class FicPerViewSet(ModelViewSet):
    queryset = mod_fic_per.FicPer.objects.all()
    serializer_class = ser_fic_per.FicPerSerializer

class AtrFicViewSet(ModelViewSet):
    queryset = mod_atr_fic.AtrFic.objects.all()
    serializer_class = ser_atr_fic.AtrFicSerializer
