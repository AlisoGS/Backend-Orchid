from rest_framework.viewsets import ModelViewSet
from core.models import mod_atr_fic
from core.serializers import ser_atr_fic

class AtrFicViewSet(ModelViewSet):
    queryset = mod_atr_fic.AtrFic.objects.all()
    serializer_class = ser_atr_fic.AtrFicSerializer