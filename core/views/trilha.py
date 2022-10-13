from rest_framework.viewsets import ModelViewSet

from core.models import Trilha
from core.serializers import TrilhaDetailSerializer, TrilhaSerializer


class TrilhaViewSet(ModelViewSet):
    queryset = Trilha.objects.all()


    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return TrilhaDetailSerializer
        return TrilhaSerializer

