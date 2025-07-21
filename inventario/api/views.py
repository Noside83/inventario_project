from rest_framework import viewsets
from inventario.models import Producto
from inventario.api.serializer import ProductoSerializer
from rest_framework.permissions import IsAuthenticated

class ProductoViewSet(viewsets.ModelViewSet):
    #implementando la autenticación con JWT
    permission_classes =[IsAuthenticated]

    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


