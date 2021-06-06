from app.models import Marca
from django.urls import path, include
from .views import home, registro, ProductoViewset, MarcaViewset, listar_productos
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', ProductoViewset)
router.register('marca', MarcaViewset)


urlpatterns = [
    path('', home, name="home"),
    path('registro/', registro, name="registro"),
    path('api/', include(router.urls)),
    path('listar-productos/', listar_productos, name="listar_productos")
]
