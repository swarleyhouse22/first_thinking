"""misitio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls,name="admin"),
    path('listas/', include('apps.listas.urls'),name="listas"),
    path('login/',include('apps.base.urls'),name="login"),
    path('logout/',include('apps.base.urls'),name="logout"),
    path('tiendas/',include('apps.tiendas.urls'),name="tiendas")
    path('productos/',include('apps.productos.urls'),name="productos"),
    path('',include('social.apps.django_app.urls'),name="social"),
    path('',include('app.base.urls'),name="base"),    
]
