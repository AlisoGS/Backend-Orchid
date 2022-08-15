from rest_framework.serializers import ModelSerializer
from core.models import mod_ficha

class FichaSerializer(ModelSerializer):
    class Meta:
        model = mod_ficha.Ficha
        fields = '__all__'