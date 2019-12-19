from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Lista
from apps.productos.models import Producto
from .forms import ListaForm

class OwnershipMixin(object):
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs
        current_user = self.request.user
        object_owner = getattr(self.get_object(), 'usuario')

        if current_user != object_owner:
            return redirect('listas:lista_list')
        return super(OwnershipMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.

@login_required(login_url='/')
def listas_list(request):
    listas = Lista.objects.filter(usuario=request.user)
    json = serializers.serialize('json', listas)    
    context = {'listas':listas, 'json':json}
    
    return render(request, 'listas/lista_list.html', context)

@login_required(login_url='/')
def agregarProducto(request):    
    if request.method == 'GET':
        lista = Lista.objects.get(id=request.GET['lista'])
        producto = Producto.objects.get(id=request.GET['producto'])

        lista.costoTotalReal = lista.costoTotalReal + producto.costoReal
        print(lista.costoTotalReal)

        lista.productos.add(producto)
        lista.save()
        return redirect('listas:lista_detail', pk=lista.id)


    return render(request, 'listas/lista_list.html')

@login_required(login_url='/')
def quitarProducto(request):    
    if request.method == 'GET':
        lista = Lista.objects.get(id=request.GET['lista'])
        producto = Producto.objects.get(id=request.GET['producto'])

        lista.costoTotalReal = lista.costoTotalReal - producto.costoReal

        lista.productos.remove(producto)                
        lista.save()
        return redirect('listas:lista_detail', pk=lista.id)


    return render(request, 'listas/lista_list.html')

class ListaDetail(OwnershipMixin, DetailView):
    model = Lista
    context_object_name = 'lista'
    template_name = 'listas/lista_detail.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['productos'] = self.object.productos.all()
        context['productosJson'] = serializers.serialize('json', self.object.productos.all()) 
        context['listaProductos'] = Producto.objects.filter(usuario=self.request.user)
        return context

class ListaCreate (LoginRequiredMixin,CreateView):
    login_url = '/login/'
    model = Lista
    form_class = ListaForm
    template_name = 'listas/lista_form.html'
    success_url = reverse_lazy('listas:lista_list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.usuario = self.request.user
        obj.save()
        return super().form_valid(form)

class ListaDelete (LoginRequiredMixin,DeleteView):
    login_url = '/login/'
    model = Lista
    template_name = 'listas/lista_delete.html'
    success_url = reverse_lazy('listas:lista_list')

class ListaUpdate (UpdateView):
    model = Lista
    form_class = ListaForm
    template_name = 'listas/lista_form.html'
    success_url = reverse_lazy('listas:lista_list')



