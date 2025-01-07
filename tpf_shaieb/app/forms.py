from django import forms
from app.models import Producto
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


# Formulario para cargar un nuevo producto
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del producto'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

# Formulario para buscar un producto por nombre
class BuscaProductoForm(forms.Form):
    nombre = forms.CharField(label="Nombre del producto", max_length=40)

class UserProfileForm(UserChangeForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

# Formulario para actualizar el avatar del usuario
