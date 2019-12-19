from django.urls import path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from .views import ListaCreate, ListaDelete, ListaUpdate, listas_list, agregarProducto, ListaDetail, quitarProducto

app_name='listas'

urlpatterns = [
    
    path('crear/',ListaCreate.as_view(),name="lista_form"),
    path('ver/<int:pk>',ListaDetail.as_view(),name="lista_detail"),
    path('editar/<int:pk>',ListaUpdate.as_view(),name="lista_update"),
    path('borrarProducto/<int:pk>',ListaDelete.as_view(),name="lista_delete"),
    path('agregar-producto',agregarProducto,name="lista_add_producto"),
    path('quitar-producto',quitarProducto,name="lista_remove_producto"),   
    path('',listas_list,name="lista_list"),
]
