from django import forms
from app.models import Producto

class ProductosFormulario(forms.Form):
    nombre=forms.CharField()
    precio=forms.IntegerField()
    categoria=forms.CharField()


class BuscaProductoForm(forms.Form):
    nombre = forms.CharField(label="Nombre del producto", max_length=40)

    