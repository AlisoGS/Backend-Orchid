from rest_framework.viewsets import ModelViewSet
from core.models import Trilha
from core.serializers import TrilhaSerializer


class TrilhaViewSet(ModelViewSet):
    queryset = Trilha.objects.all()
    serializer_class = TrilhaSerializer
