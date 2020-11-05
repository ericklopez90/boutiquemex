from django.db import models
from model_utils.models import TimeStampedModel
from applications.users.models import Usuarios

# Create your models here.

class Imagenes(TimeStampedModel):
    url = models.URLField('URL', unique=True)
    actualizado_por = models.ForeignKey(Usuarios, on_delete=models.PROTECT)
    activo = models.BooleanField(default=True)

class Documentos(TimeStampedModel):
    url = models.URLField('URL', unique=True)
    actualizado_por = models.ForeignKey(Usuarios, on_delete=models.PROTECT)
    activo = models.BooleanField(default=True)

    


