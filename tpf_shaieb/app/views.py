from django.shortcuts import render
from app.models import Producto
from app.forms import ProductosFormulario
from app.forms import BuscaProductoForm



def inicio(request):
    return render(request, "app/inicio.html")

def acerca(request):
    return render(request, "app/acerca.html")

def productos(request):
    return render(request, "app/productos.html")

def tienda(request):
    return render(request, "app/tienda.html")

def ProductosFormularioView(request):
    if request.method == 'POST':
        producto = Producto(
            nombre=request.POST['nombre'],
            precio=request.POST['precio'],
            categoria=request.POST['categoria']
        )
        producto.save()
        return render(request, "app/inicio.html")
    return render(request, "app/ProductosFormulario.html")

def form_con_api(request):
    if request.method == "POST":
        mi_formulario = ProductosFormulario(request.POST)  # Procesa la información del formulario
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            producto = Producto(
                nombre=informacion["nombre"],
                precio=informacion["precio"],
                categoria=informacion["categoria"]
            )
            producto.save()
            return render(request, "app/inicio.html")
    else:
        mi_formulario = ProductosFormulario()

    return render(request, "app/form_con_api.html", {"mi_formulario": mi_formulario})

def buscar_form_con_api(request):
    if request.method == "POST":
        mi_formulario = BuscaProductoForm(request.POST)  # Usa el nuevo formulario aquí
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            # Filtrar productos por nombre
            productos = Producto.objects.filter(nombre__icontains=informacion["nombre"])
            
            return render(request, "app/mostrar_productos.html", {"productos": productos})
    else:
        mi_formulario = BuscaProductoForm()

    return render(request, "app/buscar_form_con_api.html", {"mi_formulario": mi_formulario})


