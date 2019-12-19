from django.urls import path
from .views import TiendasList, TiendasCreate, TiendasUpdate, TiendasDelete, tiendas_list

app_name = 'tiendas'

urlpatterns = [
    
    path('crear/', TiendasCreate.as_view(), name="tiendas_form"),
    path('editar/<int:pk>', TiendasUpdate.as_view(), name="tiendas_update"),
    path('borrar/<int:pk>', TiendasDelete.as_view(), name="tiendas_delete"),
    path('', tiendas_list, name="tiendas_list"),
]