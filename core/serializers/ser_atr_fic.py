from rest_framework.serializers import ModelSerializer
from core.models import mod_atr_fic

class AtrFicSerializer(ModelSerializer):
    class Meta:
        model = mod_atr_fic.AtrFic
        fields = '__all__'