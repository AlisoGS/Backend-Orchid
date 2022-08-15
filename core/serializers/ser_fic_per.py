from rest_framework.serializers import ModelSerializer
from core.models import mod_fic_per

class FicPerSerializer(ModelSerializer):
    class Meta:
        model = mod_fic_per.FicPer
        fields = '__all__'