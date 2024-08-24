from django.shortcuts import render
from .models import Clientes, Productos, Opiniones
from django.http import HttpResponse


# Luego de importar nuestros 3 modelos, vamos a cear nuestras vistas.

def inicio(request):
    '''Será lo primero que veamos en nuestra página'''
    return render(request, 'AppMicu/index.html')

def clientes(request):
    return render(request, 'AppMicu/clientes.html')

def productos(request):
    return render(request, 'AppMicu/productos.html')

def comentarios(request):
    return render(request, 'AppMicu/comentarios.html')
