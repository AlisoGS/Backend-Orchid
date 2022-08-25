from rest_framework.viewsets import ModelViewSet
from core.models import mod_origem
from core.serializers import ser_origem

class OrigemViewSet(ModelViewSet):
    queryset = mod_origem.Origem.objects.all()
    serializer_class = ser_origem.OrigemSerializer
