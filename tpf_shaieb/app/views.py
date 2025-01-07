from django.shortcuts import render, redirect, get_object_or_404
from app.models import Producto
from app.forms import ProductoForm, BuscaProductoForm
from .forms import UserProfileForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden



def inicio(request):
    return render(request, "app/inicio.html")


def acerca(request):
    return render(request, "app/acerca.html")


# Vista para mostrar productos
@login_required
def mostrar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'app/mostrar_producto.html', {'productos': productos})


# Vista para cargar productos
@login_required
def cargar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Guarda el producto en la base de datos
            return redirect('mostrar_producto')  # Redirige a la página de productos
    else:
        form = ProductoForm()  # Muestra un formulario vacío
    return render(request, 'app/cargar_producto.html', {'form': form})

# Vista para buscar productos
@login_required
def buscar_form_con_api(request):
    if request.method == "POST":
        mi_formulario = BuscaProductoForm(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            # Filtrar productos por nombre
            productos = Producto.objects.filter(nombre__icontains=informacion["nombre"])
            return render(request, "app/mostrar_producto.html", {"productos": productos})
    else:
        mi_formulario = BuscaProductoForm()

    return render(request, "app/buscar_form_con_api.html", {"mi_formulario": mi_formulario})

@login_required
def editar_producto(request, producto_id):
    # Obtiene el producto por su ID
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()  # Guarda los cambios en el producto
            return redirect('mostrar_producto')  # Redirige a la página de productos
    else:
        form = ProductoForm(instance=producto)  # Carga el formulario con los datos del producto

    return render(request, 'app/editar_producto.html', {'form': form, 'producto': producto})

