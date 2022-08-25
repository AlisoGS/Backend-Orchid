from rest_framework.viewsets import ModelViewSet
from core.models import mod_fic_per
from core.serializers import ser_fic_per

class FicPerViewSet(ModelViewSet):
    queryset = mod_fic_per.FicPer.objects.all()
    serializer_class = ser_fic_per.FicPerSerializer

