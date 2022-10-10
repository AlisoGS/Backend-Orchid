from rest_framework.viewsets import ModelViewSet

from core.models import Arma, Utilitario, Vestimenta
from core.serializers import (
    ArmaDetailSerializer,
    ArmaSerializer,
    UtilitarioDetailSerializer,
    UtilitarioSerializer,
    VestimentaDetailSerializer,
    VestimentaSerializer,
)


class ArmaViewSet(ModelViewSet):
    queryset = Arma.objects.all()


    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ArmaDetailSerializer
        return ArmaSerializer

class UtilitarioViewSet(ModelViewSet):
    queryset = Utilitario.objects.all()


    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return UtilitarioDetailSerializer
        return UtilitarioSerializer

class VestimentaViewSet(ModelViewSet):
    queryset = Vestimenta.objects.all()


    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return VestimentaDetailSerializer
        return VestimentaSerializer