from . import views
from django.urls import path
from django.conf import settings
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LoginView, logout_then_login
from django.contrib.auth import views as views_auth

from .views import RegistroUsuario

app_name = 'base'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'),name="login"),
    path('logout/', views_auth.logout_then_login,{'login.url' : settings.LOGOUT_REDIRECT_URL},name='logout'),
    path('registro/',RegistroUsuario.as_view(),name="registro"),
    path('', views.home,name="home")
]

