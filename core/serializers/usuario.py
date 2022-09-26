from rest_framework.serializers import ModelSerializer, SlugRelatedField

from core import models
from media.models import Image
from media.serializers import ImageSerializer


class UsuarioSerializer(ModelSerializer): 
    foto_attachment_key = SlugRelatedField(
        source="foto",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    foto = ImageSerializer(required=False, read_only=True)
    class Meta:
        model = models.Usuario
        fields = "__all__"

class UsuarioDetailSerializer(ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = "__all__"
        depth = 1
    foto = ImageSerializer(required=False)