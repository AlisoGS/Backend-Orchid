from rest_framework.serializers import ModelSerializer

from core import models


class PericiaSerializer(ModelSerializer):
    class Meta:
        model = models.Pericia
        fields = "__all__"
