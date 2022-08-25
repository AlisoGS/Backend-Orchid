from rest_framework.viewsets import ModelViewSet
from core.models import fic_per
from core.serializers import ser_fic_per

class FicPerViewSet(ModelViewSet):
    queryset = fic_per.FicPer.objects.all()
    serializer_class = ser_fic_per.FicPerSerializer

