from rest_framework import serializers, pagination
from .models import Bancos, InfoBancos


class PaginationSerializer(pagination.PageNumberPagination):

    page_size = 5
    max_page_size = 50

class BancosSerializer(serializers.ModelSerializer):


    class Meta:
        model = Bancos
        fields = ('__all__')


class InfoBancosSerializer(serializers.ModelSerializer):


    class Meta:
        model = InfoBancos
        fields = ('__all__')