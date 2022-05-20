from django.db import models

class Institucion(models.Model):
    nombreInsti = models.CharField(max_length=50)
    descripcionInsti = models.TextField()
    direccionInsti = models.TextField()
    barrioInsti =  models.TextField()
    correoInsti = models.EmailField(null=True)
    telefonoInsti = models.BigIntegerField(null=True)
    telefonoFijoInsti = models.BigIntegerField(null=True)
    nit = models.BigIntegerField(primary_key=True)
    tipoZona = models.CharField(max_length=50,choices=(
        ('Urbana','Urbana'),
        ('Rural','Rural')
    ))
    sectorInsti = models.CharField(max_length=50,choices=(
        ('Privado','Privado')
        ('Oficial','Oficial')
    ))
    nombreRector =  models.CharField(max_length=50,default="")
    
