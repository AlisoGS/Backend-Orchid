from rest_framework.serializers import ModelSerializer

from core import models


class ArmaSerializer(ModelSerializer):
    class Meta:
        model = models.Arma
        fields = "__all__"

class ArmaDetailSerializer(ModelSerializer):
    class Meta:
        model = models.Arma
        fields = "__all__"
        depth = 1

class UtilitarioSerializer(ModelSerializer):
    class Meta:
        model = models.Utilitario
        fields = "__all__"


class UtilitarioDetailSerializer(ModelSerializer):
    class Meta:
        model = models.Utilitario
        fields = "__all__"
        depth = 1

class VestimentaSerializer(ModelSerializer):
    class Meta:
        model = models.Vestimenta
        fields = "__all__"

class VestimentaDetailSerializer(ModelSerializer):
    class Meta:
        model = models.Vestimenta
        fields = "__all__"
        depth = 1
