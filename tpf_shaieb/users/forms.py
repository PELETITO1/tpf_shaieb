from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm,UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']

class UserEditForm(UserCreationForm):

    # Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    # No obligatorios
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = [
            'email',
            'password1',
            'password2',
            'last_name',
            'first_name'
        ]
        help_texts = {k:"" for k in fields}
