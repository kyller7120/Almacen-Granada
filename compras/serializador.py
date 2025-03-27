from rest_framework import serializers
from .models import ListaCompra, Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class ListaCompraSerializer(serializers.ModelSerializer):
    productos = ProductoSerializer(many=True, read_only=True)

    class Meta:
        model = ListaCompra
        fields = ['id', 'nombre', 'fecha_creacion', 'productos']