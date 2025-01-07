from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.log_in, name="login"),
    path('logout/', views.log_out, name="logout"),
    path('perfil/', views.perfil, name="perfil"),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('actualizar_avatar/', views.actualizar_avatar, name='actualizar_avatar'),
    path('cambiar_contrasena/', PasswordChangeView.as_view(template_name='users/cambiar_contrasena.html'), name='cambiar_contrasena'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='app/inicio.html'), name='password_change_done')
]