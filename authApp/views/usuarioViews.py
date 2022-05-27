from urllib import response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from authApp.serializers.usuarioSerializer import UsuarioSerializer, UsuarioListSerializer
from authApp.models import Usuario

@api_view(['GET','POST'])
def usuarioViewset(request):

    if request.method == 'GET':
        users = Usuario.objects.all().values('id','email','password','es_estudiante','es_institucion')
        users_serializer = UsuarioListSerializer(users,many=True)
        return Response(users_serializer.data,status= status.HTTP_200_OK)
    
    elif request.method == 'POST':
        users_serializer = UsuarioSerializer(data=request.data)

        if users_serializer.is_valid():
             users_serializer.save()
             return Response(users_serializer.data,status.HTTP_201_CREATED)

        return Response(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def usuarioDetailView(request,pk=None):
    user = Usuario.objects.filter(id = pk).first()

    if user:

        if request.method == 'GET':
            user_serializer = UsuarioSerializer(user)
            return Response(user_serializer.data,status= status.HTTP_200_OK)

        elif request.method == 'PUT':
            user_serializer = UsuarioSerializer(user,data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data,status= status.HTTP_200_OK)

            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            user.delete()
            return Response({'message':'Usuario eliminado correctamente!'}, status= status.HTTP_200_OK)
    
    return Response({'message':'No se ha encontrado un usuario en estos datos'}, status=status.HTTP_400_BAD_REQUEST)

