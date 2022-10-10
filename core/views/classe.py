from rest_framework.viewsets import ModelViewSet

from core.models import Classe
from core.serializers import ClasseDetailSerializer, ClasseSerializer


class ClasseViewSet(ModelViewSet):
    queryset = Classe.objects.all()


    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ClasseDetailSerializer
        return ClasseSerializer