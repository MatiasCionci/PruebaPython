from django import forms
from .models import Contacto
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .validators import MaxSizeValidator
from django.forms import ValidationError


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'
    #sino ["nombre"] poner los campos q quiero asi

class UsuarioForm(forms.ModelForm):
    imagen = forms.ImageField(required=False,validators=[MaxSizeValidator(max_file_size=1)])
    nombreU = forms.CharField(min_length=3,max_length=50)

    def clean_nombreU(self):
        nombreU = self.cleaned_data["nombreU"]
        existe = Usuario.objects.filter(nombreU__iexact=nombreU).exists()
        #__iexact hace que no diferencia entre mayusculas y minusculas
        if existe:
            raise ValidationError("este usuario ya existe")

        return nombreU

    class Meta:
            model = Usuario
            fields = '__all__'

            widgets = {
                "fechaNacimiento": forms.SelectDateWidget()
            }

        # sino ["nombre"] poner los campos q quiero asi

class CustomUser(User):
    REQUIRED_FIELDS = ['email', 'password1', 'password2','username']
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(required=True, min_length=2, help_text='Required.')


    def clean_username(self):
        username = self.cleaned_data["username"]
        existe = Usuario.objects.filter(nombreU=username).exists()
            #__iexact hace que no diferencia entre mayusculas y minusculas
        if existe:

            raise ValidationError("este usuario ya existe")

        return username

    def clean_password2(self):
        pass1 = self.cleaned_data["password1"]
        pass2 = self.cleaned_data["password2"]
        if not pass1 == pass2:

            raise ValidationError("los password deben ser iguales")

        return pass1


    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('username', 'password1', 'email','password2')



 

class CustomUserContactoForm(UserCreationForm):
    class Meta:
        model = Contacto

        fields = {'nombreUsuario','email','passw','estado'}