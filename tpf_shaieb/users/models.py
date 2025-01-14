# users/models.py
from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="avatar")
    imagen = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f"Avatar de {self.user.username}"