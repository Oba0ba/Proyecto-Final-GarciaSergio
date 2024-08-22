from django.urls import path
from AppMicu import views

urlpatterns = [
    path('inicio/',views.inicio, name='inicio'),
    path('clientes/',views.clientes, name='clientes'),
    path('productos/', views.productos, name='productos'),
    path('comentario/', views.opiniones, name='comentarios')

]