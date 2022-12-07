from rest_framework.serializers import (
    ModelSerializer,
    SlugRelatedField,
    HiddenField,
    CurrentUserDefault,
)

from drf_extra_fields.fields import Base64ImageField

from core import models

class PericiaSerializer(ModelSerializer):
    class Meta:
        model = models.Pericia
        fields = ("nome",)


class FichaDetailSerializer(ModelSerializer):
    class Meta:
        model = models.Ficha
        fields = "__all__"
        depth = 2


class FicPerSerializer(ModelSerializer):
    pericia = PericiaSerializer()
    class Meta:
        model = models.FicPer
        fields = "__all__"


class FicPerPostSerializer(ModelSerializer):
    class Meta:
        model = models.FicPer
        fields = ("pericia",)


class FichaSerializer(ModelSerializer):
    pericias = FicPerPostSerializer(many=True)
    usuario = HiddenField(default=CurrentUserDefault())
    imagem = Base64ImageField()

    class Meta:
        model = models.Ficha
        fields = "__all__"

    def create(self, validated_data):
        pericias = validated_data.pop("pericias", None)
        ficha = models.Ficha.objects.create(**validated_data)

        if pericias is not None:
            for pericia in pericias:
                models.FicPer.objects.create(**pericia, ficha=ficha)

        ficha.save()
        return ficha
