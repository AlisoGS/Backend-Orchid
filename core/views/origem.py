from rest_framework.viewsets import ModelViewSet

from core.models import Origem
from core.serializers import OrigemDetailSerializer, OrigemSerializer


class OrigemViewSet(ModelViewSet):
    queryset = Origem.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return OrigemDetailSerializer
        return OrigemSerializer