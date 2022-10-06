from rest_framework.viewsets import ModelViewSet

from core.models import Ficha, FicPer
from core.serializers import FichaDetailSerializer, FichaSerializer, FicPerSerializer


class FichaViewSet(ModelViewSet):
    queryset = Ficha.objects.all()


    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return FichaDetailSerializer
        return FichaSerializer


class FicPerViewSet(ModelViewSet):

    queryset = FicPer.objects.all()
    serializer_class = FicPerSerializer