from django.db import models
from .usuario import Usuario

class Institucion(models.Model):
    idCol = models.BigIntegerField(primary_key=True)
    nombreInsti = models.CharField(max_length=50,unique=True)
    descripcionInsti = models.TextField()
    direccionInsti = models.TextField()
    barrioInsti =  models.TextField()
    localidadInsti =  models.TextField()
    correoInsti = models.EmailField(null=True)
    telefonoInsti = models.BigIntegerField(null=True)
    telefonoFijoInsti = models.BigIntegerField(null=True)
    nit = models.BigIntegerField(unique=True,null=False)
    codigoDANE = models.BigIntegerField(unique=True,null=False)
    tipoZona = models.CharField(max_length=50,choices=(
        ('Urbana','Urbana'),
        ('Rural','Rural')
    ))
    sectorInsti = models.CharField(max_length=50,choices=(
        ('Privado','Privado'),
        ('Oficial','Oficial')
    ))
    nombreRector =  models.CharField(max_length=50,default="")
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    
