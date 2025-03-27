from rest_framework import viewsets
from .models import ListaCompra, Producto
from .serializador import ListaCompraSerializer, ProductoSerializer

# ViewSet para manejar las operaciones CRUD de ListaCompra
class ListaCompraViewSet(viewsets.ModelViewSet):
    queryset = ListaCompra.objects.all()
    serializer_class = ListaCompraSerializer

# ViewSet para manejar las operaciones CRUD de Producto
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
