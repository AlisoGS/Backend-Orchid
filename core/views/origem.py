from rest_framework.viewsets import ModelViewSet
from core.models.origem import Origem
from core.serializers.origem import OrigemSerializer, OrigemDetailSerializer
from rest_framework.permissions import IsAuthenticated


class OrigemViewSet(ModelViewSet):
    queryset = Origem.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return OrigemDetailSerializer
        return OrigemSerializer