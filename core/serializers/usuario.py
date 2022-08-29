from rest_framework.serializers import ModelSerializer
from core.models import usuario

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = usuario.Usuario
        fields = '__all__'
