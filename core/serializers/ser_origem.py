from rest_framework.serializers import ModelSerializer
from core.models import mod_origem

class OrigemSerializer(ModelSerializer):
    class Meta:
        model = mod_origem.Origem
        fields = '__all__'
