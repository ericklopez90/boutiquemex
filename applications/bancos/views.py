from rest_framework import viewsets
from django.shortcuts import render
from .models import Bancos, InfoBancos
from .serializers import BancosSerializer, InfoBancosSerializer

# Create your views here.

class BancosViewSet(viewsets.ModelViewSet):
    serializer_class = BancosSerializer
    queryset = Bancos.objects.all()

class InfoBancosViewSet(viewsets.ModelViewSet):
    serializer_class = InfoBancosSerializer
    queryset = InfoBancos.objects.all()
