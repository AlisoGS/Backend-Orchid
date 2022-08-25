from rest_framework.viewsets import ModelViewSet
from core.models import origem
from core.serializers import ser_origem

class OrigemViewSet(ModelViewSet):
    queryset = origem.Origem.objects.all()
    serializer_class = ser_origem.OrigemSerializer
