from django.db import models

class ListaCompra(models.Model):
    nombre = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    lista = models.ForeignKey(ListaCompra, on_delete=models.CASCADE, related_name='productos')
    nombre = models.CharField(max_length=255)
    cantidad = models.PositiveIntegerField()
    descripcion = models.TextField(blank=True, null=True)   
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.cantidad} x {self.nombre} en {self.lista.nombre}"