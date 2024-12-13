from django import forms
from app.models import producto

class ProductosFormulario(forms.Form):
    nombre=forms.CharField()
    precio=forms.IntegerField()
    categoria=forms.CharField()


    