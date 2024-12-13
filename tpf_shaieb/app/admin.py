from django.contrib import admin
from app.models import Cliente , direccion ,fecha, producto

admin.site.register(Cliente)
admin.site.register(direccion)
admin.site.register(fecha)
admin.site.register(producto)