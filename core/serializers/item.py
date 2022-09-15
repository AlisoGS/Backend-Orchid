from rest_framework.serializers import ModelSerializer
from core import models


class ArmaSerializer(ModelSerializer):
    class Meta:
        model = models.Arma
        fields = "__all__"


class UtilitarioSerializer(ModelSerializer):
    class Meta:
        model = models.Utilitario
        fields = "__all__"


class VestimentaSerializer(ModelSerializer):
    class Meta:
        model = models.Vestimenta
        fields = "__all__"
