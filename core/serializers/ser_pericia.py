from rest_framework.serializers import ModelSerializer
from core.models import mod_pericia

class PericiaSerializer(ModelSerializer):
    class Meta:
        model = mod_pericia.Pericia
        fields = '__all__'