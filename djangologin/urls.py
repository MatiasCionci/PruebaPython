"""djangologin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from usuarios.views import index_usuarios,contacto,agregar_usuario,listar_usuario,modificar_usuario,eliminar_usuario,registro,UsuarioViewSet,index_login,index_perfil
from rest_framework import routers

router = routers.DefaultRouter()
router.register('usuario', UsuarioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_usuarios,name='index_usuarios'),
    path('loginpro/', index_login),
    path('iniPerfil/', index_perfil,name='index_perfil'),
    path('contacto/', contacto),
    path('agregar-usuario/', agregar_usuario,name="agregarusuario"),
    path('listar-usuario/', listar_usuario,name="listarusuario"),
    path('modificar-usuario/<id>/', modificar_usuario,name="modificarusuario"),
    path('eliminar-usuario/<id>/', eliminar_usuario, name="eliminarusuario"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro/', registro,name="registro"),
    path('api/', include(router.urls)),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)