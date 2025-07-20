
from rest_framework.routers import DefaultRouter
from inventario.api.views import ProductoViewSet

router = DefaultRouter()
router.register('productos',viewset=ProductoViewSet, basename='producto')
urlpatterns = router.urls




# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import ProductoViewSet

# router = DefaultRouter()
# router.register(r'productos', ProductoViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]