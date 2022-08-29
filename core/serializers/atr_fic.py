from rest_framework.serializers import ModelSerializer
from core.models import atr_fic

class AtrFicSerializer(ModelSerializer):
    class Meta:
        model = atr_fic.AtrFic
        fields = '__all__'