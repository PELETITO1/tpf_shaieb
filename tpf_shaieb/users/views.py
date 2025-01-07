from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, AvatarForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from users.models import Avatar
from users.forms import AvatarForm, UserProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

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
def editar_perfil(request):
    user = request.user
    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect('perfil')  # Redirige al perfil después de la edición
    else:
        user_form = UserProfileForm(instance=user)
    
    return render(request, 'users/editar_perfil.html', {'user_form': user_form})

# Vista para editar el avatar del usuario
@login_required
def actualizar_avatar(request):
    user = request.user
    try:
        avatar = Avatar.objects.get(user=user)
    except Avatar.DoesNotExist:
        avatar = None

    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=avatar)
        if form.is_valid():
            # Si se está creando o actualizando un avatar, asignamos el usuario
            avatar = form.save(commit=False)
            avatar.user = user  # Asignamos el usuario al avatar
            avatar.save()
            return redirect('perfil')
    else:
        form = AvatarForm(instance=avatar)

    return render(request, 'users/actualizar_avatar.html', {'form': form})
@login_required
def perfil(request):
    # Obtener el usuario autenticado
    user = request.user
    
    # Si el usuario tiene un avatar, lo pasamos al contexto
    avatar = user.avatar if hasattr(user, 'avatar') else None

    return render(request, 'users/perfil.html', {'user': user, 'avatar': avatar})

class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    template_name = "users/cambiar_contrasena.html"
    success_url = reverse_lazy('login')  

    def form_valid(self, form):
        
        response = super().form_valid(form)
        
        logout(self.request)
        return response