from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, AvatarForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Avatar
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
# Vista para registrar usuarios
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})

# Vista para iniciar sesión
def log_in(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Obtén al usuario autenticado
            user = form.get_user()  # Esto devuelve al usuario autenticado
            login(request, user)  # Ahora llamas a login() con el usuario
            return redirect('/')  # Redirige al inicio u otra página
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})
# Vista para cerrar sesión
def log_out(request):
    logout(request)
    return redirect("inicio")

# Vista para actualizar avatar
@login_required
def actualizar_avatar(request):
    avatar, created = Avatar.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES, instance=avatar)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = AvatarForm(instance=avatar)
    return render(request, "users/actualizar_avatar.html", {"form": form})