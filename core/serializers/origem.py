from rest_framework.serializers import ModelSerializer
from core.models import origem


class OrigemSerializer(ModelSerializer):
    class Meta:
        model = origem.Origem
        fields = "__all__"
