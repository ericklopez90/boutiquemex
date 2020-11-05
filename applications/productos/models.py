from django.db import models
from model_utils.models import TimeStampedModel
from applications.users.models import Usuarios
from applications.imagenes.models import Imagenes, Documentos
from applications.bancos.models import InfoBancos

# Create your models here.

class TipoProductos(TimeStampedModel):
    nombre = models.CharField('Nombre',max_length=40)
    actualizado_por = models.ForeignKey(Usuarios, on_delete=models.PROTECT)
    activo = models.BooleanField(default=True)


class Generos(TimeStampedModel):
    nombre = models.CharField('Nombre', max_length=10)
    actualizado_por = models.ForeignKey(Usuarios, on_delete=models.PROTECT)
    activo = models.BooleanField(default=True)


class Temporadas(TimeStampedModel):
    nombre = models.CharField('Nombre', max_length=10)
    titulo = models.CharField('Titulo', max_length=200)
    subtitulo = models.CharField('Subtitulo', max_length=200)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    actualizado_por = models.ForeignKey(Usuarios, on_delete=models.PROTECT)
    activo = models.BooleanField(default=True)


class Proveedores(TimeStampedModel):
    nombre = models.CharField('Nombre', max_length=40)
    ap_paterno = models.CharField('Apellido Paterno', max_length=50)
    email = models.EmailField('Email', unique=True)
    genero = models.IntegerField('Genero', )
    telefono = models.CharField('Telefono', max_length=12)
    identificacion = models.ForeignKey(Documentos, on_delete=models.PROTECT, related_name='identificación')
    razon_social = models.CharField('Razon social', max_length=100, unique=True)
    razon_social_doc = models.ForeignKey(Documentos, on_delete=models.PROTECT, related_name='razon_social_doc')
    nombre_marca = models.CharField('Nombre de Marca', max_length=50)
    hecho_mexicano = models.ForeignKey(Documentos, on_delete=models.PROTECT, related_name='hecho_mexicano')
    calle = models.CharField('Calle', max_length=200)
    no_ext = models.CharField('N° Exterior', max_length=6)
    no_int = models.CharField('N° Interior', max_length=6)
    cp = models.IntegerField()
    direccion_comercial = models.BooleanField('Dirección comercial', default=True)
    com_calle = models.CharField('Comercial calle', max_length=200)
    com_no_ext = models.CharField('Comercial N° exterior', max_length=6)
    com_cp = models.IntegerField()
    info_banco = models.ForeignKey(InfoBancos, on_delete=models.PROTECT)
    actualizado_por = models.ForeignKey(Usuarios, on_delete=models.PROTECT)
    activo = models.BooleanField(default=True)


class Productos(TimeStampedModel):
    tipo_producto = models.ManyToManyField(TipoProductos)
    es_para = models.ManyToManyField(Generos)
    proveedor = models.ManyToManyField(Proveedores)
    titulo = models.CharField('Titulo', max_length=100)
    subtitulo = models.CharField('Subtitulo', max_length=100)
    temporada = models.ManyToManyField(Temporadas)
    cantidad = models.IntegerField('Cantidad')
    costo = models.DecimalField('Costo', max_digits=7, decimal_places=2)
    descuento = models.DecimalField('Descuento', max_digits=7, decimal_places=2)
    imagen = models.ManyToManyField(Imagenes)
    actualizado_por = models.ForeignKey(Usuarios, on_delete=models.PROTECT)
    activo = models.BooleanField(default=True)

