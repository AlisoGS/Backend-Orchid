from rest_framework.viewsets import ModelViewSet
from core.models import item
from core.serializers import ser_item


class ArmaViewSet(ModelViewSet):
    queryset = item.Arma.objects.all()
    serializer_class = ser_item.ArmaSerializer

class UtilitarioViewSet(ModelViewSet):
    queryset = item.Utilitario.objects.all()
    serializer_class = ser_item.UtilitarioSerializer

class VestimentaViewSet(ModelViewSet):
    queryset = item.Vestimenta.objects.all()
    serializer_class = ser_item.VestimentaSerializer
