from django.db import models
from model_utils.models import TimeStampedModel
from applications.users.models import Usuarios


# Create your models here.

class Bancos(TimeStampedModel):
    nombre = models.CharField('Nombre', max_length=10)
    digito = models.IntegerField()
    actualizado_por = models.ForeignKey(Usuarios, on_delete=models.PROTECT)
    activo = models.BooleanField(default=True)


class InfoBancos(TimeStampedModel):
    banco = models.ForeignKey(Bancos, on_delete=models.PROTECT)
    no_cuenta = models.CharField('N° de cuenta', max_length=20)
    clabe = models.CharField('Clabe', max_length=20)
    no_tarjeta = models.CharField('N° de Tarjeta', max_length=16)
    nombre = models.CharField('Nombre', max_length=100)
    actualizado_por = models.ForeignKey(Usuarios, on_delete=models.PROTECT)
    activo = models.BooleanField(default=True)