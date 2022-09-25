from rest_framework.viewsets import ModelViewSet

from core.models import Proficiencia
from core.serializers import ProficienciaSerializer


class ProficienciaViewSet(ModelViewSet):
    queryset = Proficiencia.objects.all()
    serializer_class = ProficienciaSerializer

