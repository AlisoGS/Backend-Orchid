from rest_framework.serializers import ModelSerializer
from core.models import fic_per

class FicPerSerializer(ModelSerializer):
    class Meta:
        model = fic_per.FicPer
        fields = '__all__'