from rest_framework.serializers import ModelSerializer
from core.models import atributo

class AtributoSerializer(ModelSerializer):
    class Meta:
        model = atributo.Atributo
        fields = '__all__'