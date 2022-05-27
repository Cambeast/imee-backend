from rest_framework import generics

from authApp.models.institucion import Institucion
from authApp.serializers import InstitucionSerializer

class InstitucionListAPIView(generics.ListCreateAPIView):
    serializer_class = InstitucionSerializer
    queryset = Institucion.objects.all()

class InstitucionRetriveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer
