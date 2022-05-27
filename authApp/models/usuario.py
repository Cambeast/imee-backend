from msilib.schema import Property
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Usuario debe tener un email')
        
        email = self.normalize_email(email)
        user = self.model(email=email)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email,password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class Usuario(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField('Correo electronico',max_length=255,unique=True)
    es_estudiante = models.BooleanField('Estudiante status', default=False)
    es_institucion = models.BooleanField('Institución status', default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'


