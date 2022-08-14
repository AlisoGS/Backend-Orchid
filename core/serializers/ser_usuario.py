from rest_framework.serializers import ModelSerializer
from core.models import mod_usuario

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = mod_usuario.Usuario
        fields = '__all__'
