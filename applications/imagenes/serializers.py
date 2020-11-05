from rest_framework import serializers, pagination
from .models import Imagenes, Documentos


class PaginationSerializer(pagination.PageNumberPagination):

    page_size = 5
    max_page_size = 50

class ImagenesSerializer(serializers.ModelSerializer):


    class Meta:
        model = Imagenes
        fields = ('__all__')


class DocumentosSerializer(serializers.ModelSerializer):


    class Meta:
        model = Documentos
        fields = ('__all__')