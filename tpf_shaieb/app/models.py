from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField( max_length=20)
    email = models.EmailField(max_length=40 , default='aaa@aaa.com')
    

class direccion(models.Model):
    direccion = models.CharField(max_length=40)
    codigopostal = models.IntegerField(default= 'not null')

class fecha(models.Model):
    nombre = models.CharField(max_length=40)
    fecha = models.DateField()
    
    
class producto(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField(default= 'not null')
    categoria= models.CharField(max_length=40)
