from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    usuario = forms.CharField(max_length=20)
    correo_electronico = forms.EmailField()
    telefono = forms.IntegerField()

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    imagen = forms.ImageField(label="Foto", required=False)

class ComentarioForm(forms.Form):
    nombre_apellido = forms.CharField(max_length=80)
    comentario = forms.CharField(widget=forms.Textarea)

class ProductosCargados(forms.Form):
    resultado_busqueda = forms.CharField(max_length=100)
