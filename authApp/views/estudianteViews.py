from ast import Return
from rest_framework import views, status
from rest_framework.response import Response
from authApp.models import Estudiante
from authApp.serializers import EstudianteSerializer
from rest_framework import generics
from authApp.authentication_mixins import Authentication

class TestViews(views.APIView):

    def get(self, request):
        code = status.HTTP_200_OK
        data = {"message":"Prueba de mensaje"}
        return Response(data, status=code)

    def post(self, request):
        print("Creando usuario")
        print("Informacion recibida: ", request.data)
        code = status.HTTP_201_CREATED
        return Response(status=code)

class EstudianteView(views.APIView):

    def get(self, request):
        queryset = Estudiante.objects.all() 
        serialized = EstudianteSerializer(queryset, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
class EstudianteListCreateView(Authentication,generics.ListCreateAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class EstudianteRetriveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
