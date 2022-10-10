from rest_framework.serializers import ModelSerializer

from core import models


class ClasseSerializer(ModelSerializer):
    class Meta:
        model = models.Classe
        fields = "__all__"

class ClasseDetailSerializer(ModelSerializer):
    class Meta:
        model = models.Classe
        fields = "__all__"
        depth = 2