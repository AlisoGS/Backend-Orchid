from rest_framework.viewsets import ModelViewSet
from core.models import mod_ficha
from core.serializers import ser_ficha

class FichaViewSet(ModelViewSet):
    queryset = mod_ficha.Ficha.objects.all()
    serializer_class = ser_ficha.FichaSerializer
