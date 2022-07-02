from statistics import mode
from django.db import models

# Create your models here.

class Productos(models.Model):                       ### Productos es el nombre que va a tener la tabla en tu base de datos
    nombre = models.CharField(max_length=30)
    descripcion =models.CharField(max_length=30)   ### creando dato varchar
    stock = models.CharField(max_length=30)    ###  creando booleano
    precio = models.CharField(max_length=30)   ### CREANDO DATO FECHA
    imagen = models.CharField(max_length=30)   #### CREANDO DATO CORREO 

class Productos2(models.Model):                       ### Productos es el nombre que va a tener la tabla en tu base de datos
    nombre2 = models.CharField(max_length=300)
    descripcion2 =models.CharField(max_length=100)   ### creando dato varchar
    stock2 = models.CharField(max_length=300)    ###  creando booleano
    precio2 = models.CharField(max_length=300)   ### CREANDO DATO FECHA
    imagen2 = models.CharField(max_length=300) 

class Usuario(models.Model):                       ### Productos es el nombre que va a tener la tabla en tu base de datos
    run = models.CharField(max_length=300)
    nombres =models.CharField(max_length=300)   ### creando dato varchar
    apellidoPaterno = models.CharField(max_length=300)    ###  creando booleano
    apellidoMaterno = models.CharField(max_length=300)   ### CREANDO DATO FECHA
    email = models.CharField(max_length=300)  
    teléfono = models.CharField(max_length=300) #### CREANDO DATO CORREO 
    mensaje = models.CharField(max_length=300)
    