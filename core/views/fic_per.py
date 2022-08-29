from rest_framework.viewsets import ModelViewSet
from core.models import fic_per
from core.serializers.fic_per import FicPerSerializer

class FicPerViewSet(ModelViewSet):
    queryset = fic_per.FicPer.objects.all()
    serializer_class = FicPerSerializer

