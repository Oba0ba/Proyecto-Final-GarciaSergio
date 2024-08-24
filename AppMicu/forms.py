#from django import forms

# def curso_form(req):

#     if req.method == 'POST':

      

#             curso =  Curso(nombre=req.POST['curso'],camada=req.POST['camada'])

 

#             curso.save()

 

#             return render(req, "AppCoder/index.html")

 

#     return render(req,"AppCoder/cursoFormulario.html").

# def curso_form_2(request):

 

#       if request.method == "POST":

 

#             miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html

#             print(miFormulario)

 

#             if miFormulario.is_valid:

#                   informacion = miFormulario.cleaned_data

#                   curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])

#                   curso.save()

#                   return render(request, "AppCoder/index.html")

#       else:

#             miFormulario = CursoFormulario()

 

#       return render(request, "AppCoder/curso_formulario_2.html", {"miFormulario": miFormulario})