from rest_framework.serializers import ModelSerializer
from core.models import pericia


class PericiaSerializer(ModelSerializer):
    class Meta:
        model = pericia.Pericia
        fields = "__all__"
