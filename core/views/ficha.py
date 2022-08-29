from rest_framework.viewsets import ModelViewSet
from core.models import ficha
from core.serializers.ficha import FichaSerializer

class FichaViewSet(ModelViewSet):
    queryset = ficha.Ficha.objects.all()
    serializer_class = FichaSerializer
