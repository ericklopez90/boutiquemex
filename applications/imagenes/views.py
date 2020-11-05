from rest_framework import viewsets
from django.shortcuts import render
from .models import Imagenes, Documentos
from .serializers import ImagenesSerializer, DocumentosSerializer

# Create your views here.

class ImagenesViewSet(viewsets.ModelViewSet):
    serializer_class = ImagenesSerializer
    queryset = Imagenes.objects.all()

class DocumentosViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentosSerializer
    queryset = Documentos.objects.all()
