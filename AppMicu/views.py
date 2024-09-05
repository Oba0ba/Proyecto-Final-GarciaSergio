from django.shortcuts import render
from .models import Clientes, Productos, Opiniones
from django.http import HttpResponse
from .forms import ClienteForm, ProductoForm, ComentarioForm, ProductosCargados
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



# Luego de importar nuestros 3 modelos, vamos a cear nuestras vistas.

# def inicio(request):
#     '''Será lo primero que veamos en nuestra página'''
#     return render(request, 'AppMicu/index.html')

class InicioView(TemplateView):
    template_name = 'AppMicu/index.html'

def nosotros(request):
    return render(request, 'AppMicu/sobre_nosotros.html')

@login_required
def cliente_form(request):
    if request.method == 'POST':
        cliente_formulario = ClienteForm(request.POST) 
        print (cliente_formulario)     
        
        if cliente_formulario.is_valid:
            informacion = cliente_formulario.cleaned_data
            cliente = Clientes (nombre=informacion['nombre'], apellido=informacion['apellido'], usuario=informacion['usuario'], correo_electronico=informacion['correo_electronico'], telefono=informacion['telefono'])
            cliente.save()
            return render(request, "AppMicu/index.html")
   
    else:   
        cliente_formulario= ClienteForm()
        return render(request, "AppMicu/clientesForm.html", {"cliente_formulario": cliente_formulario})

@login_required    
def producto_form(request):
    if request.method == 'POST':
        producto_formulario = ProductoForm(request.POST) 
        print (producto_formulario)     
        
        if producto_formulario.is_valid:
            informacion = producto_formulario.cleaned_data
            producto = Productos (nombre=informacion['nombre'], precio=informacion['precio'])
            producto.save()
            return render(request, "AppMicu/index.html")
   
    else:   
        producto_formulario= ProductoForm()
        return render(request, "AppMicu/productosForm.html", {"producto_formulario": producto_formulario})


def comentario_form(request):
    if request.method == 'POST':
        comentario_formulario = ComentarioForm(request.POST) 
        print (comentario_formulario)     
        
        if comentario_formulario.is_valid:
            opinion = Opiniones(
                nombre_apellido=comentario_formulario.cleaned_data['nombre_apellido'],
                comentario=comentario_formulario.cleaned_data['comentario']
            )
            opinion.save()
            return render(request, "AppMicu/index.html")
   
    else:   
        comentario_formulario= ComentarioForm()
        return render(request, "AppMicu/comentariosForm.html", {"comentario_formulario": comentario_formulario})

@login_required        
def mostrar_producto_form(request):
    productos = Productos.objects.all()

    contexto = {"productos":productos}
    return render(request, "AppMicu/productoscargados.html", contexto)