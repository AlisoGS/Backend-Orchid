from rest_framework.serializers import ModelSerializer
from core.models import mod_atributo

class AtributoSerializer(ModelSerializer):
    class Meta:
        model = mod_atributo.Atributo
        fields = '__all__'