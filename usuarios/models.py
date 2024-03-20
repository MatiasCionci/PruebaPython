from django.db import models

# Create your models here.
class Loginn(models.Model):
    nombre = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
def __str__(self):
    return self.nombre

class Usuario(models.Model):
    nombreU = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fechaNacimiento = models.DateField()
    mail = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="usuariosima",null=True)
   # log = models.ForeignKey(Loginn,on_delete=models.CASCADE)
    #se puede poner cascade para q cuando eliminar de login a tdo el usuario
def __str__(self):
    return self.nombreU


opciones_estados = [
    (0,"soltero"),
    (1,"novio"),
    (2,"casado"),

]
class Contacto(models.Model):
    nombreUsuario = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    estado = models.IntegerField(choices=opciones_estados,null=True)
    passw = models.CharField(max_length=50)

def __str__(self):
    return self.nombreUsuario