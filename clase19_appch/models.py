from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre=models.CharField(max_length=100)
    camada=models.IntegerField()

    def __str__(self):
        return f"Curso: {self.nombre} / Comision: {self.camada}"

class Estudiante(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()

class Profesor(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    profesion=models.CharField(max_length=50)

class Entregable(models.Model):
    nombre=models.CharField(max_length=50)
    FechaDeEntrega=models.DateField()
    entregado=models.BooleanField()