from django.urls import path
from AppMicu import views
from AppMicu.views import InicioView   


urlpatterns = [
    path('', InicioView.as_view(), name='inicio'),
    path('agregar-cliente/',views.cliente_form, name='agregar cliente'),
    path('agregar-producto/',views.ProductoCreateView.as_view(), name='New'),
    path('productos-cargados/',views.ProductoListView.as_view(), name='List'),
    path('clases/detalle/<int:pk>/', views.ProductoDetalle.as_view(), name='Detail'),
    path('clases/editar/<int:pk>', views.ProductoUpdateView.as_view(), name='Edit'),
    path('clases/eliminar/<int:pk>', views.ProductoDeleteView.as_view(), name='Delete'),
    path('comentarios/', views.comentario_form, name='comentarios'),
    path('sobrenosotros/', views.nosotros, name='nosotros')
]