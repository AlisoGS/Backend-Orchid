from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from core.models import Ficha, FicAtr, FicPer
from core.serializers import (
    FichaSerializer,
    FicPerSerializer,
    FicAtrSerializer,
    FichaDetailSerializer,
)


class FichaViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Ficha.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return FichaDetailSerializer
        return FichaSerializer


class FicPerViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = FicPer.objects.all()
    serializer_class = FicPerSerializer


class FicAtrViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = FicAtr.objects.all()
    serializer_class = FicAtrSerializer
