from rest_framework import viewsets
from django.shortcuts import render
from .models import Usuarios
from .serializers import UsuariosSerializer

# Create your views here.

class UsuariosViewSet(viewsets.ModelViewSet):
    serializer_class = UsuariosSerializer
    queryset = Usuarios.objects.all()
