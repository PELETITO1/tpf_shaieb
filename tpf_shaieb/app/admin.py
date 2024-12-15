from django.contrib import admin
from app.models import Cliente , Direccion ,Fecha, Producto

admin.site.register(Cliente)
admin.site.register(Direccion)
admin.site.register(Fecha)
admin.site.register(Producto)