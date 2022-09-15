from rest_framework.viewsets import ModelViewSet
from core.models import Proficiencia
from core.serializers import ProficienciaSerializer
from rest_framework.permissions import IsAuthenticated


class ProficienciaViewSet(ModelViewSet):
    queryset = Proficiencia.objects.all()
    serializer_class = ProficienciaSerializer
    permission_classes = [IsAuthenticated]

