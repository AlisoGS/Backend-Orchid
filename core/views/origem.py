from rest_framework.viewsets import ModelViewSet
from core.models.origem import Origem
from core.serializers.origem import OrigemSerializer, OrigemDetailSerializer


class OrigemViewSet(ModelViewSet):
    queryset = Origem.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return OrigemDetailSerializer
        return OrigemSerializer