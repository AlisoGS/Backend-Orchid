from rest_framework.serializers import ModelSerializer
from core.models import ficha


class FichaSerializer(ModelSerializer):
    class Meta:
        model = ficha.Ficha
        fields = "__all__"


class FicPerSerializer(ModelSerializer):
    class Meta:
        model = ficha.FicPer
        fields = "__all__"
