from django.urls import include, path
from rest_framework import routers
from .views import ListaCompraViewSet

rutass = routers.DefaultRouter()
rutass.register(r'listaCompra', ListaCompraViewSet)

urlpatterns = [
    path('', include(rutass.urls))
]