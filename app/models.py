from django.db import models
from django.db.models.deletion import PROTECT

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre  

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    nuevo = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete=PROTECT)
    imagen = models.CharField(max_length=255, null=True)
    stock = models.IntegerField(default=0)


    def __str__(self):
        return self.nombre    