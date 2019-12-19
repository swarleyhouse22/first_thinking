from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponseRedirect

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Producto
from .forms import ProductosForm
from apps.listas.models import Lista

from django.contrib.auth.mixins import LoginRequiredMixin

class OwnershipMixin(object):
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs
        current_user = self.request.user
        object_owner = getattr(self.get_object(), 'usuario')

        if current_user != object_owner:
            return redirect('productos:productos_list')
        return super(OwnershipMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.

class ProductoList (LoginRequiredMixin,ListView):
    login_url = '/login/'
    model = Producto
    template_name = 'productos/producto_list.html'

@login_required(login_url='/')
def productos_list(request):
    productos = Producto.objects.filter(usuario=request.user)
    context = {'productos':productos}
    
    return render(request, 'productos/producto_list.html', context)

class ProductoCreate (LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Producto
    
    form_class = ProductosForm
    template_name = 'productos/producto_form.html'

    def get_success_url(self):
        next = self.request.GET.get('next', '')
        id = self.request.GET.get('id', '0')
        if next == 'listas':
            if id != '0':
                self.success_url = reverse_lazy('listas:lista_detail', args=[id])
            else:
                self.success_url = reverse_lazy('listas:lista_list')
        else:
            self.success_url = reverse_lazy('productos:producto_list')    
        return self.success_url

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(ProductoCreate, self).form_valid(form)

    def get_form_kwargs(self):
       kwargs = super().get_form_kwargs()
       kwargs.update({'request': self.request})
       return kwargs

class ProductoUpdate (OwnershipMixin, UpdateView):

    login_url = '/login/'
    model = Producto    
    form_class = ProductosForm
    template_name = 'productos/producto_form.html'

    def get_success_url(self):
        next = self.request.GET.get('next', '')
        id = self.request.GET.get('id', '0')
        if next == 'listas':
            if id != '0':
                self.success_url = reverse_lazy('listas:lista_detail', args=[id])
            else:
                self.success_url = reverse_lazy('listas:lista_list')
        else:
            self.success_url = reverse_lazy('productos:producto_list')    
        return self.success_url

    def get_form_kwargs(self):
       kwargs = super().get_form_kwargs()
       kwargs.update({'request': self.request})
       return kwargs

    def form_valid(self, form):
        producto = Producto.objects.get(id=self.object.id)
        listas = producto.lista_set.all()
        for lista in listas:
            lista.costoTotalReal = lista.costoTotalReal - producto.costoReal        
        for lista in listas:
            lista.costoTotalReal = lista.costoTotalReal + self.object.costoReal
            lista.save()
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

class ProductoDelete (OwnershipMixin,DeleteView):

    login_url = '/login/'
    model = Producto
    template_name = 'productos/producto_delete.html'
    success_url = reverse_lazy('productos:producto_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        listas = self.object.lista_set.all()
        for lista in listas:
            lista.costoTotalReal = lista.costoTotalReal - self.object.costoReal        
            lista.save()
        print(listas)
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())