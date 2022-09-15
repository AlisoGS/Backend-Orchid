from rest_framework.viewsets import ModelViewSet
from core.models import Poder
from core.serializers import PoderSerializer
from rest_framework.permissions import IsAuthenticated


class PoderViewSet(ModelViewSet):
    queryset = Poder.objects.all()
    serializer_class = PoderSerializer
    permission_classes = [IsAuthenticated]