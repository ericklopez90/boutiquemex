from rest_framework import serializers, pagination
from .models import Usuarios


class PaginationSerializer(pagination.PageNumberPagination):

    page_size = 5
    max_page_size = 50

class UsuariosSerializer(serializers.ModelSerializer):


    class Meta:
        model = Usuarios
        fields = ('__all__')