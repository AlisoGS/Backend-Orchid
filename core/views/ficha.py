from rest_framework.viewsets import ModelViewSet
from core.models import ficha
from core.serializers.ficha import FichaSerializer, FicPerSerializer, FicAtrSerializer


class FichaViewSet(ModelViewSet):
    queryset = ficha.Ficha.objects.all()
    serializer_class = FichaSerializer


class FicPerViewSet(ModelViewSet):
    queryset = ficha.FicPer.objects.all()
    serializer_class = FicPerSerializer

class FicAtrViewSet(ModelViewSet):
    queryset = ficha.FicAtr.objects.all()
    serializer_class = FicAtrSerializer
