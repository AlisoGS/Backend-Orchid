from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from core.models.ficha import Ficha, FicAtr, FicPer
from core.serializers.ficha import FichaSerializer, FicPerSerializer, FicAtrSerializer, FichaDetailSerializer

class FichaViewSet(ModelViewSet):
    queryset = Ficha.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
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
