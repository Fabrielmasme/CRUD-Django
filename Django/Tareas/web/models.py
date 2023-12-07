from django.db import models

#Lo que se hace es definir los modelos de las tablas que va a haber dentro de la base de datos, con sus campos.

class producto(models.Model):
    nombre_producto = models.CharField(max_length=100, verbose_name='Producto')
    descripcion = models.CharField(max_length=200, verbose_name='Descripcion')

    def __str__(self):
        return f"{self.nombre_producto} {self.descripcion}"