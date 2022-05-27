from rest_framework import serializers
from authApp.models.usuario import Usuario

class UsuarioTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('email',)

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
    
    def create(self, validated_data):
        user = Usuario(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        updated_user = super().update(instance, validated_data)
        updated_user.set_password(validated_data['password'])
        updated_user.save()
        return updated_user
        
class UsuarioListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'Correo elecronico': instance['email'],
            'contraseña': instance['password'],
            'Cuenta de estudiante': instance['es_estudiante'],
            'Cuenta de institución': instance['es_institucion']
        }
    

