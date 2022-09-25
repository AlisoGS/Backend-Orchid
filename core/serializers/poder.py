from rest_framework.serializers import ModelSerializer

from core import models


class PoderSerializer(ModelSerializer):
    class Meta:
        model = models.Poder
        fields = "__all__"
