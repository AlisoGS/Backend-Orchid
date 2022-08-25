from rest_framework.viewsets import ModelViewSet
from core.models import mod_item
from core.serializers import ser_item


class ArmaViewSet(ModelViewSet):
    queryset = mod_item.Arma.objects.all()
    serializer_class = ser_item.ArmaSerializer

class UtilitarioViewSet(ModelViewSet):
    queryset = mod_item.Utilitario.objects.all()
    serializer_class = ser_item.UtilitarioSerializer

class VestimentaViewSet(ModelViewSet):
    queryset = mod_item.Vestimenta.objects.all()
    serializer_class = ser_item.VestimentaSerializer
