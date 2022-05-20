from django.contrib import admin
from .models.estudiante import Estudiante
from .models.acudiente import Acudiente

# Register your models here.

admin.site.register(Estudiante)
admin.site.register(Acudiente)