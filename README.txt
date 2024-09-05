Aplicación de sitio web para tienda de venta de pastas caseras.
importar librerias -- leer requirements.txt

En la App Micu, tendremos:
Una página de 'inicio' que será nuestra página padre, donde podremos ver los artículos que ofrece la tienda. (http://127.0.0.1:8000/)

Podremos modificar la base de datos, agregando clientes en la página' agregar cliente' (http://127.0.0.1:8000/agregar-cliente/) y también podemos agregar productos en la página 'agregar productos'(http://127.0.0.1:8000/agregar-producto/).
También podemos consultar la lista de productos que tenemos cargados en nuestra base de datos en la página 'Lista de productos' (http://127.0.0.1:8000/productos-cargados/).

Para ingresar a la base de datos, usar el superusuario.
(http://127.0.0.1:8000/admin/)
usuario: admin
contraseña: admin






otros datos sin relevancia:
source entorno_web/Scripts/activate
cd web_proyecto
python manage.py runserver