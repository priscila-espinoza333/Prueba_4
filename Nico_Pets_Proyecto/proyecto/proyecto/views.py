from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from base_de_datos.models import Productos
from base_de_datos.models import Productos2
from django.shortcuts import render, redirect
from base_de_datos.models import Usuario


def inicio(request):
    return render(request,"index.html")

def contacto(request):
    return render(request,"contacto.html") 

def galeria(request):
    return render(request,"galeria.html")

def login(request):
    return render(request,"login.html")

def productos(request):
    productos = Productos2.objects.all 
    contexto = {'datos':productos,}
    return render(request,"productos.html", contexto)

def seguimiento(request):
    productos = Productos2.objects.all 
    contexto = {'datos':productos,}
    return render(request,"seguimiento.html", contexto)  

def historial(request):
    return render(request,"historial.html") 

def Register(request):
    return render(request,"register.html") 
          
def usuarioLogueado(request):
    correo = f'se ha logueado el usuario {request.GET["email"]}'
    contraseña = f'se ha logueado el usuario {request.GET["contraseña"]}'
    contexto = {'mail':correo,'pass':contraseña,}
    return render(request,"usuario_logueado.html", contexto)   

def load_contacto(request):
    print('mantenedorcontacto.py -> load_contacto')    
    print('method -> ', request.method)
    if request.method == 'GET':
        try:
            auth, error = authorization(request, 'delete_contacto')
            if not auth:
                redirect(error)
            codigo = request.GET['codigo']
            print('codigo -> ', codigo)
            contacto = Usuario.objects.get(pk=codigo)
            contacto.delete()
        except Exception as e:
            print(e)
    if request.method == 'POST':
        try:
            #Lectura Formulario
            id = request.POST['codigo']
            nombres = request.POST['nombres']
            apellidoPaterno = request.POST['apellidoPaterno']
            apellidoMaterno = request.POST['apellidoMaterno']
            email = request.POST['email']
            telefono = request.POST['telefono']            
            asunto = request.POST['asunto']
            #Busqueda de objecto en la base de datos
            contacto = Usuario.objects.get(pk=id)
            #Actualizando objeto en memoria volatil
            contacto.nombres = nombres
            contacto.apellidoPaterno = apellidoPaterno
            contacto.apellidoMaterno = apellidoMaterno            
            contacto.email = email            
            contacto.telefono = telefono            
            contacto.asunto = asunto  
            #Actualizando en la base de datos                      
            contacto.save(force_update=True)
        except Exception as e:
            print(e)
    contactos = Usuario.objects.all
    return render(request, 'mantenedor-contacto.html', {'contactos': contactos})     


        



