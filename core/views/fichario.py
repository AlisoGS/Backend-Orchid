from rest_framework.viewsets import ModelViewSet

from core.models import Fichario
from core.serializers import FicharioDetailSerializer, FicharioSerializer


class FicharioViewSet(ModelViewSet):
    queryset = Fichario.objects.all()


    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return FicharioDetailSerializer
        return FicharioSerializer
