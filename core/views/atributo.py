from rest_framework.viewsets import ModelViewSet
from core.models import  mod_atributo
from core.serializers import ser_atributo

class AtributoViewSet(ModelViewSet):
    queryset = mod_atributo.Atributo.objects.all()
    serializer_class = ser_atributo.AtributoSerializer
