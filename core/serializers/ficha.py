from rest_framework.serializers import ModelSerializer
from core.models import ficha


class FichaSerializer(ModelSerializer):
    class Meta:
        model = ficha.Ficha
        fields = "__all__"

class FichaDetailSerializer(ModelSerializer):
    class Meta:
        model = ficha.Ficha
        fields = "__all__"
        depth = 2

class FicPerSerializer(ModelSerializer):
    class Meta:
        model = ficha.FicPer
        fields = "__all__"


class FicAtrSerializer(ModelSerializer):
    class Meta:
        model = ficha.FicAtr
        fields = "__all__"
