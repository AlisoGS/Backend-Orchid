from rest_framework.viewsets import ModelViewSet
from core.models import pericia
from core.serializers.pericia import PericiaSerializer
from rest_framework.permissions import IsAuthenticated


class PericiaViewSet(ModelViewSet):
    queryset = pericia.Pericia.objects.all()
    serializer_class = PericiaSerializer
    permission_classes = [IsAuthenticated]
