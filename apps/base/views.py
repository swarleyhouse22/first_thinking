from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

from .forms import RegistroForm

# Create your views here.


class RegistroUsuario(CreateView):
    model = get_user_model()
    form_class = RegistroForm
    template_name = "registro.html"
    success_url = reverse_lazy('base:home')

def home(request):
    return render (request,'home.html')
