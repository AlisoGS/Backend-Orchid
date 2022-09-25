from rest_framework.viewsets import ModelViewSet
from core.models import Poder
from core.serializers import PoderSerializer


class PoderViewSet(ModelViewSet):
    queryset = Poder.objects.all()
    serializer_class = PoderSerializer
