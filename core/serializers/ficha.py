from rest_framework.serializers import ModelSerializer

from core import models


class FichaSerializer(ModelSerializer):
    class Meta:
        model = models.Ficha
        fields = "__all__"

class FichaDetailSerializer(ModelSerializer):
    class Meta:
        model = models.Ficha
        fields = "__all__"
        depth = 2

class FicPerSerializer(ModelSerializer):
    class Meta:
        model = models.FicPer
        fields = "__all__"


class FicAtrSerializer(ModelSerializer):
    class Meta:
        model = models.FicAtr
        fields = "__all__"
