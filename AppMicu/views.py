from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Clientes, Productos, Opiniones
from django.http import HttpResponse
from .forms import ClienteForm, ProductoForm, ComentarioForm, ProductosCargados
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView  # Para mostrar detalles de un objeto
from django.views.generic.edit import CreateView, UpdateView, DeleteView  # Para crear, actualizar y eliminar objetos
from django.urls import reverse_lazy  # Para generar URLs de forma segura


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


class ProductoListView(LoginRequiredMixin, ListView):
    """
    Vista para mostrar una lista de todos los productos.
    """
    model = Productos  # Modelo con el que trabaja esta vista
    template_name = "AppMicu/productoscargados.html"  # Plantilla para renderizar la lista

    def get_queryset(self):
        return Productos.objects.order_by('nombre')

class ProductoDetalle(LoginRequiredMixin, DetailView):
    """
    Vista para mostrar los detalles de un producto específico.
    """
    model = Productos
    template_name = "AppMicu/productosdetalle.html"

class ProductoCreateView(LoginRequiredMixin, CreateView):
    """
    Vista para crear nuevos productos a través de un formulario.
    """
    model = Productos
    template_name = "AppMicu/productosForm.html"
    success_url = reverse_lazy("List")  # URL de redirección después de crear un curso
    fields = ["nombre", "precio", "imagen"]  # Campos del modelo a mostrar en el formulario

class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    """
    Vista para editar productos existentes a través de un formulario
    """
    model = Productos
    template_name = "AppMicu/productoseditar.html"
    success_url = reverse_lazy("List")
    #success_url = "/AppCoder/clases/lista/"  # Otra forma de especificar la URL de redirección
    fields = ["nombre", "precio", "imagen"]

class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    """
    Vista para eliminar cursos.
    """
    model = Productos
    success_url = reverse_lazy("List")  # URL de redirección después de eliminar un curso
    template_name = "AppMicu/productos_confirm_delete.html"  # Plantilla para confirmar la eliminación