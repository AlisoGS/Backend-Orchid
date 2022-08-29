from rest_framework.viewsets import ModelViewSet
from core.models import atr_fic
from core.serializers.atr_fic import AtrFicSerializer

class AtrFicViewSet(ModelViewSet):
    queryset = atr_fic.AtrFic.objects.all()
    serializer_class = AtrFicSerializer