from django.urls import path
from AppMicu import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('clientes/',views.clientes, name='clientes'),
    path('agregar-cliente/',views.cliente_form, name='agregar cliente'),
    path('productos/', views.productos, name='productos'),
    path('agregar-producto/',views.producto_form, name='agregar producto'),
    path('productos-cargados/',views.mostrar_producto_form, name='Lista de productos'),
    path('comentarios/', views.comentario_form, name='comentarios')
]