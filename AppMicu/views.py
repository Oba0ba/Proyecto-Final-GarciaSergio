from django.shortcuts import render
from .models import Clientes, Productos, Opiniones
from django.http import HttpResponse

# Luego de importar nuestros 3 modelos, vamos a cear nuestras vistas.

def inicio(request):
    '''Será lo primero que veamos en nuestra página'''
    return HttpResponse('Inicio')
    #return render(req, 'appcoder/padre.html')

def clientes(request):
       return HttpResponse('Clientes')
    #return render(req, 'appcoder/padre.html')

def productos(request):
    return HttpResponse('Productos')
    #return render(req, 'appcoder/padre.html')

def opiniones(request):
    return HttpResponse('Opiniones')
    #return render(req, 'appcoder/padre.html')
