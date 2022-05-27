from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.sessions.models import Session
from datetime import datetime
from rest_framework.views import APIView

from authApp.serializers.usuarioSerializer import UsuarioTokenSerializer

class Usertoken(APIView):
    def get(self, request, *args, **kwargs):
        username = request.GET.get('username')
        try:
            user_token = Token.objects.get(
                user = UsuarioTokenSerializer().Meta.model.objects.filter(username = username).first()
            )
            return Response({'token': user_token.key})
        except:
            return Response({'error': 'credenciales enviadas incorrectas'},status=status.HTTP_400_BAD_REQUEST)

class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data = request.data, context = {'request':request})
        
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token,created = Token.objects.get_or_create(user = user)
                user_serializer = UsuarioTokenSerializer(user)
                if created:
                    return Response({'token':token.key,'user':user_serializer.data,'message': 'Inicio exitoso'}, status=status.HTTP_201_CREATED)
                else:
                    all_sesions = Session.objects.filter(expire_date__gte = datetime.now())
                    if all_sesions.exists():
                        for session in all_sesions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()
                    token.delete()
                    token = Token.objects.create(user = user)
                    return Response({'token':token.key,'user':user_serializer.data,'message': 'Inicio exitoso'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error':'Este usuario no puede iniciar sesión'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error':'email o contraseña incorrecto'}, status=status.HTTP_400_BAD_REQUEST)

class Logout(APIView):
    
    def post(self,request,*args,**kwargs):
        try:
            token = request.GET.get('token')
            token = Token.objects.filter(key=token).first()
            if token:
                user = token.user
                all_sesions = Session.objects.filter(expire_date__gte = datetime.now())
                if all_sesions.exists():
                    for session in all_sesions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
                token.delete()

                session_message = 'sesiones de usuario eliminadas.'
                token_message = 'Token eliminado'
                return Response({'token_message': token_message, 'session_message': session_message}, status=status.HTTP_200_OK)
            return Response({'error':'no se ha encontrado el usuario con las credenciales'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            Response({'error':'no se ha encontrado token en la peticion'}, status=status.HTTP_409_CONFLICT)



