from django.urls import path
from AppMicu import views
from AppMicu.views import InicioView   


urlpatterns = [
    path('', InicioView.as_view(), name='inicio'),
    path('agregar-cliente/',views.cliente_form, name='agregar cliente'),
    path('agregar-producto/',views.producto_form, name='agregar producto'),
    path('productos-cargados/',views.mostrar_producto_form, name='Lista de productos'),
    path('comentarios/', views.comentario_form, name='comentarios'),
    path('sobrenosotros/', views.nosotros, name='nosotros')
]