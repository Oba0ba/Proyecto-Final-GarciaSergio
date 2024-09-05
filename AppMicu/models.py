from django.db import models


class Clientes(models.Model):
    '''Aquí llevaremos registro de los datos de nuestros clientes'''
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    usuario = models.CharField(max_length=20)
    correo_electronico = models.EmailField()
    telefono = models.IntegerField()

    def __str__(self):
        return f'Cliente: {self.nombre} {self.apellido}\nUsuario: {self.usuario}\nCorreo electrónico: {self.correo_electronico}\nTeléfono: {self.telefono}'
    

class Productos(models.Model):
    '''Detalle de los artículos y sus precios correspondientes'''
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to= 'imagenes', null = True)
    
    def __str__(self):
        return f'Producto: {self.nombre}; Precio: ${self.precio}'
    

class Opiniones(models.Model):
    '''Para llevar un registro de las experiencias de nuestros clientes'''
    nombre_apellido = models.CharField(max_length=80)
    comentario = models.TextField()

    def __str__(self):
        return f'Comentario escrito por {self.nombre_apellido}: "{self.comentario}"'