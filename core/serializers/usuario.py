from rest_framework.serializers import ModelSerializer

from core import models


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = "__all__"
