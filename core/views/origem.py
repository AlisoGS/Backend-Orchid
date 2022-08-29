from rest_framework.viewsets import ModelViewSet
from core.models import origem
from core.serializers.origem import OrigemSerializer

class OrigemViewSet(ModelViewSet):
    queryset = origem.Origem.objects.all()
    serializer_class = OrigemSerializer
