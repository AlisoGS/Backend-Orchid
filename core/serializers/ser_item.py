from rest_framework.serializers import ModelSerializer
from core.models import mod_item

class ArmaSerializer(ModelSerializer):
    class Meta:
        model = mod_item.Arma
        fields = '__all__'

class UtilitarioSerializer(ModelSerializer):
    class Meta:
        model = mod_item.Utilitario
        fields = '__all__'
    
class VestimentaSerializer(ModelSerializer):
    class Meta:
        model = mod_item.Vestimenta
        fields = '__all__'
