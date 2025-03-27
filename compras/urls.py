from django.urls import include, path
from rest_framework import routers
from .views import ListaCompraViewSet

rutas = routers.DefaultRouter()
rutas.register(r'listaCompra', ListaCompraViewSet)

urlpatterns = [
    path('', include(rutas.urls))
]