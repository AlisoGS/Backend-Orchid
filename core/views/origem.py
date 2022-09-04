from rest_framework.viewsets import ModelViewSet
from core.models.origem import Origem
from core.serializers.origem import OrigemSerializer


class OrigemViewSet(ModelViewSet):
    queryset = Origem.objects.all()
    serializer_class = OrigemSerializer
