from rest_framework.viewsets import ModelViewSet
from core.models import Pericia
from core.serializers import PericiaSerializer
from rest_framework.permissions import IsAuthenticated


class PericiaViewSet(ModelViewSet):
    queryset = Pericia.objects.all()
    serializer_class = PericiaSerializer
    permission_classes = [IsAuthenticated]
