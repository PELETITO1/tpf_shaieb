from django.urls import path
from app import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('acerca/', views.acerca, name="acerca"),
    path('productos/', views.mostrar_productos, name='mostrar_producto'),
    path('cargar_producto/', views.cargar_producto, name='cargar_producto'),
    path('productos/buscar/', views.buscar_form_con_api, name='buscar_producto'),
    path('productos/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    
]
