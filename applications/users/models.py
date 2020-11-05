from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.

class Usuarios(AbstractBaseUser):
    nombre = models.CharField(max_length=40)
    ap_paterno = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    genero = models.IntegerField()
    telefono = models.CharField(max_length=12, blank=True, null=True)
    activo = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'