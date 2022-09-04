from rest_framework.viewsets import ModelViewSet
from core.models import ficha
from core.serializers.ficha import FichaSerializer, FicPerSerializer


class FichaViewSet(ModelViewSet):
    queryset = ficha.Ficha.objects.all()
    serializer_class = FichaSerializer


class FicPerViewSet(ModelViewSet):
    queryset = ficha.FicPer.objects.all()
    serializer_class = FicPerSerializer
