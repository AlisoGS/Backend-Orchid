from rest_framework.serializers import ModelSerializer

from core import models


class AtributoSerializer(ModelSerializer):
    class Meta:
        model = models.Atributo
        fields = "__all__"
