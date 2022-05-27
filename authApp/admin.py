from django.contrib import admin

from authApp.models.usuario import Usuario
from .models.estudiante import Estudiante
from .models.acudiente import Acudiente
from .models.institucion import Institucion

# Register your models here.

admin.site.register(Estudiante)
admin.site.register(Acudiente)
admin.site.register(Usuario)
admin.site.register(Institucion)