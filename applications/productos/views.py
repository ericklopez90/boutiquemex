from rest_framework import viewsets
from django.shortcuts import render
from .models import Productos, Proveedores, Temporadas, TipoProductos, Generos
from .serializers import (
    ProductosSerializer,
    ProveedoresSerializer,
    TemporadasSerializer,
    TipoProductosSerializer,
    GenerosSerializer
)

# Create your views here.

class ProductosViewSet(viewsets.ModelViewSet):
    serializer_class = ProductosSerializer
    queryset = Productos.objects.all()


class ProveedoresViewSet(viewsets.ModelViewSet):
    serializer_class = ProveedoresSerializer
    queryset = Proveedores.objects.all()


class TemporadasViewSet(viewsets.ModelViewSet):
    serializer_class = TemporadasSerializer
    queryset = Temporadas.objects.all()


class TipoProductosViewSet(viewsets.ModelViewSet):
    serializer_class = TipoProductosSerializer
    queryset = TipoProductos.objects.all()


class GenerosViewSet(viewsets.ModelViewSet):
    serializer_class = GenerosSerializer
    queryset = Generos.objects.all()