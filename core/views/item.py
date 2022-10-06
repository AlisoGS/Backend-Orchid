from rest_framework.viewsets import ModelViewSet

from core.models import Arma, Utilitario, Vestimenta
from core.serializers import ArmaSerializer, UtilitarioSerializer, VestimentaSerializer


class ArmaViewSet(ModelViewSet):
    queryset = Arma.objects.all()
    serializer_class = ArmaSerializer


class UtilitarioViewSet(ModelViewSet):
    queryset = Utilitario.objects.all()
    serializer_class = UtilitarioSerializer


class VestimentaViewSet(ModelViewSet):
    queryset = Vestimenta.objects.all()
    serializer_class = VestimentaSerializer