from django.db import models

class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    tipoIdent = models.CharField(max_length=50,choices=(
        ('TD','Tarjeta de identidad'),
    ))
    identificacion = models.BigIntegerField()
    nombres = models.CharField(max_length=50,default="")
    apellidos = models.CharField(max_length=50,default="")
    fechaNacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=50)
    direccion = models.TextField()
    barrio =  models.TextField()
    localidad =  models.TextField()
    telefono = models.BigIntegerField(null=True)
    nivelSisben = models.PositiveSmallIntegerField()
    puntajeSisben = models.FloatField()
    eps = models.CharField(max_length=30)
    tipoSanguinio = models.CharField(max_length=50,choices=(
        ('A','A'),
        ('B','B'),
        ('O','O'),
        ('AB','AB')  
    ))
    rh = models.CharField(max_length=50,choices=(
        ('Positivo','+'),
        ('Negativo','-'),
    ))
    genero = models.CharField(max_length=50,choices=(
        ('Masculino','M',),
        ('Femenino','F',), 
        ('Sin definir','Sin definir'),
    ))
    matriculado = models.BooleanField(default=False)







