from rest_framework.serializers import (
    ModelSerializer,
    SlugRelatedField,
    HiddenField,
    CurrentUserDefault,
)

from core import models


class FichaDetailSerializer(ModelSerializer):
    class Meta:
        model = models.Ficha
        fields = "__all__"
        depth = 2


class FicPerSerializer(ModelSerializer):
    class Meta:
        model = models.FicPer
        fields = "__all__"


class FichaSerializer(ModelSerializer):
    pericias = FicPerSerializer(many=True)
    usuario = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = models.Ficha
        fields = "__all__"

    def create(self, validated_data):
        pericias = validated_data.pop("pericias", None)
        ficha = models.Ficha.objects.create(**validated_data)

        if pericias is not None:
            for pericia in pericias:
                models.FicPer.objects.create(pericia=pericia, ficha=ficha)

        ficha.save()
        return ficha
