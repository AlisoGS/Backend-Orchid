from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from core.models import Arma, Utilitario, Vestimenta
from core.serializers import ArmaSerializer, UtilitarioSerializer, VestimentaSerializer


class ArmaViewSet(ModelViewSet):
    queryset = Arma.objects.all()
    serializer_class = ArmaSerializer
    permission_classes = [IsAuthenticated]


class UtilitarioViewSet(ModelViewSet):
    queryset = Utilitario.objects.all()
    serializer_class = UtilitarioSerializer
    permission_classes = [IsAuthenticated]


class VestimentaViewSet(ModelViewSet):
    queryset = Vestimenta.objects.all()
    serializer_class = VestimentaSerializer
    permission_classes = [IsAuthenticated]
