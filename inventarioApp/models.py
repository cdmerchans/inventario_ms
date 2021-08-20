from django.db import models

class Producto(models.Model):
    
    id_producto = models.BigAutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length = 50, unique =  True)
    precio = models.IntegerField('Precio')
    descripcion = models.CharField('Descripción', max_length = 200)
    cantidad = models.IntegerField('Cantidad')
    categoria = models.CharField('Categoría', max_length = 50)
