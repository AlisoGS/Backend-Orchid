from rest_framework.serializers import ModelSerializer
from core.models import ficha

class FichaSerializer(ModelSerializer):
    class Meta:
        model = ficha.Ficha
        fields = '__all__'