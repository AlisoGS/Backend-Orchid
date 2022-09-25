from rest_framework.serializers import ModelSerializer

from core import models


class OrigemSerializer(ModelSerializer):
    class Meta:
        model = models.Origem
        fields = "__all__"

class OrigemDetailSerializer(ModelSerializer):
    class Meta:
        model = models.Origem
        fields = "__all__"
        depth = 1