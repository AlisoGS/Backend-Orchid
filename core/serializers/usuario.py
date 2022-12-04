from rest_framework.serializers import ModelSerializer, SlugRelatedField

from core import models


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = "__all__"

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance


class UsuarioDetailSerializer(ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = (
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "data_nascimento",
            "foto",
        )
        depth = 1
