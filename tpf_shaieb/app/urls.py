from django.urls import path
from app import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('acerca/', views.acerca, name="acerca"),
    path('productos/', views.productos, name="productos"),
    path('tienda/', views.tienda, name="tienda"),
    path('productosformulario/', views.ProductosFormularioView, name="ProductosFormulario"),
    path('form_con_api/', views.form_con_api, name="FormConApi"),
]
