from rest_framework.serializers import ModelSerializer
from core.models import proficiencia

class ProficienciaSerializer(ModelSerializer):
    class Meta:
        model = proficiencia.Proficiencia
        fields = '__all__'