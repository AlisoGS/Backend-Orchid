from rest_framework.viewsets import ModelViewSet
from core.models.ficha import Ficha, FicAtr, FicPer
from core.serializers.ficha import FichaSerializer, FicPerSerializer, FicAtrSerializer, FichaDetailSerializer

class FichaViewSet(ModelViewSet):
    queryset = Ficha.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return FichaDetailSerializer
        return FichaSerializer

class FicPerViewSet(ModelViewSet):
    queryset = FicPer.objects.all()
    serializer_class = FicPerSerializer

class FicAtrViewSet(ModelViewSet):
    queryset = FicAtr.objects.all()
    serializer_class = FicAtrSerializer
