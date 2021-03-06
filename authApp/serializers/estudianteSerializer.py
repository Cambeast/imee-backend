from rest_framework import serializers
from authApp.models.estudiante import Estudiante
from .usuarioSerializer import UsuarioSerializer

class EstudianteSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField()

    class Meta:
        model = Estudiante
        fields = '__all__'