from rest_framework.viewsets import ModelViewSet

from core.models import Ficha, FicPer
from core.serializers import FichaDetailSerializer, FichaSerializer, FicPerSerializer


class FichaViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return FichaDetailSerializer
        return FichaSerializer

    def get_queryset(self):
        usuario = self.request.user

        return Ficha.objects.filter(usuario=usuario)


class FicPerViewSet(ModelViewSet):

    queryset = FicPer.objects.all()
    serializer_class = FicPerSerializer
