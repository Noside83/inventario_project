from rest_framework import serializers
from inventario.models import Producto
#20:18 
class ProductoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__' 