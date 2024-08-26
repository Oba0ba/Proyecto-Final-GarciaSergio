from django.contrib import admin
from .models import Clientes, Productos, Opiniones

admin.site.register(Clientes)
admin.site.register(Productos)
admin.site.register(Opiniones)