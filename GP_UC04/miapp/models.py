from email.policy import default
from django.db import models
 
# Create your models here.
class Estudiante(models.Model):
    codigo = models.CharField(max_length=100)
    dni = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apepat = models.CharField(max_length=100)
    apemat = models.CharField(max_length=100)
    direccion = models.TextField()
    estado = models.BooleanField()
    # auto_now_add me permitirá registrar 
    # la fecha cuando cree el registro
    creado = models.DateTimeField(auto_now_add=True)
    # auto_now me permitirá registrar 
    # la fecha cuando se modifique el registro
    actualizado = models.DateTimeField(auto_now=True)
 
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    # DateField() para guardar la fecha manualmente
    creado = models.DateField()
