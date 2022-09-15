from rest_framework.viewsets import ModelViewSet
from core.models import Trilha
from core.serializers import TrilhaSerializer
from rest_framework.permissions import IsAuthenticated


class TrilhaViewSet(ModelViewSet):
    queryset = Trilha.objects.all()
    serializer_class = TrilhaSerializer
