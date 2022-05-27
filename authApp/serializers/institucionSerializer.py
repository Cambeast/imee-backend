from rest_framework import serializers
from authApp.models.institucion import Institucion
from .usuarioSerializer import UsuarioSerializer

class InstitucionSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField()

    class Meta:
        model = Institucion
        fields = '__all__'