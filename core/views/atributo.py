from rest_framework.viewsets import ModelViewSet
from core.models import atributo
from core.serializers import AtributoSerializer
from rest_framework.permissions import IsAuthenticated


class AtributoViewSet(ModelViewSet):
    queryset = atributo.Atributo.objects.all()
    serializer_class = AtributoSerializer
