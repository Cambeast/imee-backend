from rest_framework import serializers
from authApp.models.estudiante import Estudiante

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ['id','identificacion','nombres','apellidos','matriculado','telefono']