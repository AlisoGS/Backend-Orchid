from rest_framework.viewsets import ModelViewSet
from core.models import proficiencia
from core.serializers.proficiencia import ProficienciaSerializer
from rest_framework.permissions import IsAuthenticated


class ProficienciaViewSet(ModelViewSet):
    queryset = proficiencia.Proficiencia.objects.all()
    serializer_class = ProficienciaSerializer
    permission_classes = [IsAuthenticated]

