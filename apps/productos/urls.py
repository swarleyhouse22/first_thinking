from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import ProductoList, ProductoCreate, ProductoDelete, ProductoUpdate, productos_list

app_name='productos'

urlpatterns = [
    
    path('crearProducto/', ProductoCreate.as_view(), name="producto_form"),
    path('listarProducto/',productos_list, name="producto_list"), 
    path('editarProducto/<int:pk>', ProductoUpdate.as_view(), name="producto_update"),
    path('borrarProducto/<int:pk>', ProductoDelete.as_view(), name="producto_delete")
]
