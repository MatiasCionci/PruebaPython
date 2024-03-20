from django.contrib import admin
from .models import Loginn,Usuario
from .forms import UsuarioForm
from django.contrib.auth.forms import UserCreationForm


# Register your models here.
admin.site.register(Loginn)
admin.site.register(Usuario)

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = []