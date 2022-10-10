from rest_framework.serializers import ModelSerializer

from core import models


class FicharioSerializer(ModelSerializer):
    class Meta:
        model = models.Classe
        fields = "__all__"

class FicharioDetailSerializer(ModelSerializer):
    class Meta:
        model = models.Classe
        fields = "__all__"
        depth = 2