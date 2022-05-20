from django.db import models

class Institucion(models.Model):
    nombreInsti = models.CharField(max_length=50)
    descripcionInsti = models.TextField()
    direccionInsti = models.TextField()
    correoInsti = models.EmailField(null=True)
    telefonoInsti = models.BigIntegerField(null=True)
    nit = models.BigIntegerField(primary_key=True)