from rest_framework.serializers import ModelSerializer
from core.models import item

class ArmaSerializer(ModelSerializer):
    class Meta:
        model = item.Arma
        fields = '__all__'

class UtilitarioSerializer(ModelSerializer):
    class Meta:
        model = item.Utilitario
        fields = '__all__'
    
class VestimentaSerializer(ModelSerializer):
    class Meta:
        model = item.Vestimenta
        fields = '__all__'
