from rest_framework import serializers, pagination
from .models import Productos, Proveedores, Temporadas, Generos, TipoProductos

class PaginationSerializer(pagination.PageNumberPagination):

    page_size = 5
    max_page_size = 50

class ProductosSerializer(serializers.ModelSerializer):


    class Meta:
        model = Productos
        fields = ('__all__')


class ProveedoresSerializer(serializers.ModelSerializer):


    class Meta:
        model = Proveedores
        fields = ('__all__')


class TemporadasSerializer(serializers.ModelSerializer):


    class Meta:
        model = Temporadas
        fields = ('__all__')


class GenerosSerializer(serializers.ModelSerializer):


    class Meta:
        model = Generos
        fields = ('__all__')


class TipoProductosSerializer(serializers.ModelSerializer):


    class Meta:
        model = TipoProductos
        fields = ('__all__')