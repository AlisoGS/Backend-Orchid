from rest_framework.serializers import ModelSerializer

from core import models


class TrilhaSerializer(ModelSerializer):
    class Meta:
        model = models.Trilha
        fields = "__all__"

class TrilhaDetailSerializer(ModelSerializer):
    class Meta:
        model = models.Trilha
        fields = "__all__"
        depth = 2