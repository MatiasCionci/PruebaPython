from django.shortcuts import render,redirect,get_object_or_404
from .forms import ContactoForm,UsuarioForm,CustomUserCreationForm,CustomUserContactoForm
from .models import Usuario
from django.contrib import messages
from django.contrib.auth import authenticate,login
from rest_framework import viewsets
from .serializers import UsuarioSerializer
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.forms import ValidationError
from django.core.mail import send_mail

# Create your views here.
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

def index_login(request):
    return render(request,'usuario/loginpro.html')
def index_perfil(request):
    return render(request,'iniPerfil/index.html')
def index_usuarios(request):
    context = {

        'titulo': 'index loggin'
    }
    return render(request,'index2.html',context)

def agregar_usuario(request):
    data = {
        'form': UsuarioForm()
    }
    if request.method == 'POST':
    # cuando regresa el formulario
        formularior = UsuarioForm(data=request.POST,files=request.FILES)
        if formularior.is_valid():
            formularior.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formularior

    return render(request,'usuario/agregar.html',data)
def contacto(request):


    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        #cuando regresa el formulario
        formulario = ContactoForm(data=request.POST)


    messages.success(request, 'se a enviado tu mensaje')


    return render(request,'contacto.html',data)

def listar_usuario(request):
    usuarios = Usuario.objects.all()
    data = {
        'usuarios': usuarios
    }

    return render(request,'usuario/listar.html',data)

def modificar_usuario(request,id):
    usuario = get_object_or_404(Usuario,id=id)
    data = {
        'form': UsuarioForm(instance=usuario)
    }
    if request.method == 'POST':
    # cuando regresa el formulario
        formularior = UsuarioForm(data=request.POST, instance=usuario , files=request.FILES)
        if formularior.is_valid():
            formularior.save()
            messages.success(request,"modificado correctamente")
            data["mensaje"] = "moficado correctamente"
            return redirect(to="listarusuario")
        data["form"] = formularior
    return render(request,'usuario/modificar.html',data)

def eliminar_usuario(request,id):
    usuario = get_object_or_404(Usuario,id=id)
    usuario.delete()
    return redirect(to = "listarusuario")
def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
 
    if request.method == 'POST':
     
        formulario = CustomUserCreationForm(data=request.POST,files=request.FILES)


        # __iexact hace que no diferencia entre mayusculas y minusculas

        if formulario.is_valid():
            messages.success(request, 'despues del if')
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password1=formulario.cleaned_data["password1"])
            login(request,user)
            ##
            send_mail(
                'Título del correo',
                'Hola, ete has registrado con la app gracias estaremos en contacto pronto 🐍',
                settings.EMAIL_HOST_USER,
                [formulario.cleaned_data["email"]],
                fail_silently=False
            )
            ##
            messages.success(request,"se ha enviado el mail correctamente")
            return redirect(to="/")

        data["form"] = formulario


    return render(request,'registration/registro.html',data)