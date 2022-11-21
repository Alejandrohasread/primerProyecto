from django.db import models

# Create your models here.
class usuariosDjango(models.Model):
    nombre = models.CharField(max_length=64,default='')
    apellido = models.CharField(max_length=64,default='')
    edad = models.CharField(max_length=64,default='')

class autos(models.Model):
    marca = models.CharField(max_length=128,default='')
    modelo = models.CharField(max_length=96,default='')
    kilometraje = models.CharField(max_length=32,default='')
    precio = models.CharField(max_length=32,default='')    