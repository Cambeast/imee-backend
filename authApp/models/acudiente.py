from django.db import models
from .estudiante import Estudiante

class Acudiente(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.OneToOneField(
        Estudiante,
        related_name="Acudiente",
        on_delete=models.CASCADE,
        null=True,
    )
    NomAcu = models.CharField(max_length=50)
    ideAcu = models.BigIntegerField()
    direccionAcu = models.TextField()
    fechaNacAcu = models.DateField()
    telAcu = models.BigIntegerField(null=True)
    nomPadre = models.CharField(max_length=50,null=True)
    idePadre = models.BigIntegerField(null=True)
    correoPadre = models.EmailField(null=True)
    telPadre = models.BigIntegerField(null=True)
    nomMadre = models.CharField(max_length=50,null=True)
    ideMadre = models.BigIntegerField(null=True)
    correoMadre = models.EmailField(null=True)
    telMadre = models.BigIntegerField(null=True)
