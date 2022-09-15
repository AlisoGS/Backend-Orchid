from rest_framework.serializers import ModelSerializer
from core import models


class ProficienciaSerializer(ModelSerializer):
    class Meta:
        model = models.Proficiencia
        fields = "__all__"
