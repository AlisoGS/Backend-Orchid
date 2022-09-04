from rest_framework.viewsets import ModelViewSet
from core.models import proficiencia
from core.serializers.proficiencia import ProficienciaSerializer


class ProficienciaViewSet(ModelViewSet):
    queryset = proficiencia.Proficiencia.objects.all()
    serializer_class = ProficienciaSerializer
