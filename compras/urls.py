from django.urls import include, path
from rest_framework import routers
from .views import ListaCompraViewSet

router = routers.DefaultRouter()
router.register(r'listaCompra', ListaCompraViewSet)

urlpatterns = [
    path('', include(router.urls))
]