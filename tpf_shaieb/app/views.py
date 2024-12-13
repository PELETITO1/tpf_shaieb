from django.shortcuts import render
from app.models import producto
from app.forms import ProductosFormulario

def inicio(request):
    return render(request, "app/inicio.html")

def acerca(request):
    return render(request, "app/acerca.html")

def productos(request):
    return render(request, "app/productos.html")

def tienda(request):
    return render(request, "app/tienda.html")



def ProductosFormulario(request):
    if request.method == 'POST':
        productos = productos(nombre=request.POST['nombre'],precio=request.POST['precio'], categoria=request.POST['categoria'])
        curso.save()
        return render(request, "app/index.html")
    return render(request,"app/ProductosFormulario.html")

def form_con_api(request):
    if request.method == "POST":
        mi_formulario = ProductosFormulario(request.POST)  # Aquí me llega la información del HTML
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            producto = ProductosFormulario (  Nombre=informacion["Nombre"], Precio=informacion["Precio"], Categoria=informacion["Categoria"])
            producto.save()
            return render(request, "app/index.html") 
    else:
        mi_formulario = ProductosFormulario(request)

    return render(request, "app/form_con_api.html", {"mi_formulario": mi_formulario}) 


