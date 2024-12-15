from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40, default='aaa@aaa.com')

class Direccion(models.Model):
    direccion = models.CharField(max_length=40)
    codigopostal = models.IntegerField()

class Fecha(models.Model):
    nombre = models.CharField(max_length=40)
    fecha = models.DateField()

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField()
    categoria = models.CharField(max_length=40)
