from rest_framework.viewsets import ModelViewSet

from core.models import Pericia
from core.serializers import PericiaSerializer


class PericiaViewSet(ModelViewSet):
    queryset = Pericia.objects.all()
    serializer_class = PericiaSerializer

