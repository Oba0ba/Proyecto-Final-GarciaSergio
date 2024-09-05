from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from users.forms import UserEditForm, UserRegisterForm
from users.models import Imagen
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

def login_request(request):

    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "AppMicu/index.html")

        msg_login = "Usuario o contraseña incorrectos."

    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})

def register(request):

    msg_register = ""
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Si los datos ingresados en el form son válidos, con form.save()
            # creamos un nuevo user usando esos datos
            form.save()
            return render(request,"AppMicu/index.html")
        
        msg_register = "Error en los datos ingresados. Intentalo de nuevo."

    form = UserRegisterForm()     
    return render(request,"users/registro.html" ,  {"form":form, "msg_register": msg_register})


# Vista de editar el perfil
@login_required
def editar_perfil(request):
    """
    Función de vista para manejar la edición del perfil de usuario.
    """

    # El usuario debe estar logueado para editar su perfil. 
    # Al estar logueado, podemos encontrar la instancia del usuario dentro de la solicitud -> request.user
    usuario = request.user  

    if request.method == 'POST':  # Verificar si la solicitud es un POST (envío de formulario)
        # Crear una instancia del formulario y llenarla con datos de la solicitud
        # y la instancia del usuario actual
        miFormulario = UserEditForm(request.POST, request.FILES, instance=usuario) 

        if miFormulario.is_valid():  # Validar los datos del formulario
            if miFormulario.cleaned_data.get('imagen'):  # Verificar si se subió una imagen
                if Imagen.objects.filter(user=usuario).exists():  # Si el usuario ya tiene una imagen
                    # Actualizar la imagen existente
                    usuario.imagen.imagen = miFormulario.cleaned_data.get('imagen')
                    usuario.imagen.save()  
                else:
                    # Crear un nuevo objeto de imagen y asociarlo con el usuario
                    avatar = Imagen(user=usuario, imagen=miFormulario.cleaned_data.get('imagen'))
                    avatar.save()  

            miFormulario.save()  # Guardar los datos del formulario (incluyendo cualquier otra actualización del perfil)

            return render(request, "AppMicu/Index.html")  # Redirigir a la plantilla 'padre.html'

    else:  # Si la solicitud es un GET (carga inicial de la página)
        # Crear una instancia del formulario con los datos del usuario actual pre-llenados
        miFormulario = UserEditForm(instance=usuario) 

    # Renderizar la plantilla 'editar_usuario.html', pasando el formulario y los datos del usuario
    return render(request, "users/editar_usuario.html", {"mi_form": miFormulario, "usuario": usuario})


class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = "users/editar_pass.html"
    success_url = reverse_lazy("EditarPerfil")