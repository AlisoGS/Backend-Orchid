from rest_framework.serializers import ModelSerializer, SlugRelatedField

from core import models


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = "__all__"

class UsuarioDetailSerializer(ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = "__all__"
        depth = 1