from rest_framework.viewsets import ModelViewSet
from core.models import item
from core.serializers.item import ArmaSerializer, UtilitarioSerializer, VestimentaSerializer

class ArmaViewSet(ModelViewSet):
    queryset = item.Arma.objects.all()
    serializer_class = ArmaSerializer

class UtilitarioViewSet(ModelViewSet):
    queryset = item.Utilitario.objects.all()
    serializer_class = UtilitarioSerializer

class VestimentaViewSet(ModelViewSet):
    queryset = item.Vestimenta.objects.all()
    serializer_class = VestimentaSerializer
