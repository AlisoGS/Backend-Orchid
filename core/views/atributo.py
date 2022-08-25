from rest_framework.viewsets import ModelViewSet
from core.models import  atributo
from core.serializers import ser_atributo

class AtributoViewSet(ModelViewSet):
    queryset = atributo.Atributo.objects.all()
    serializer_class = ser_atributo.AtributoSerializer
