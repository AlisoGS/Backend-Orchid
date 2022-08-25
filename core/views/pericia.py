from rest_framework.viewsets import ModelViewSet
from core.models import pericia
from core.serializers import ser_pericia

class PericiaViewSet(ModelViewSet):
    queryset = pericia.Pericia.objects.all()
    serializer_class = ser_pericia.PericiaSerializer