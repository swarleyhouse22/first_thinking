from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

from .models import Tienda, TiendaForm

class OwnershipMixin(object):
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.args = args
        self.kwargs = kwargs
        current_user = self.request.user
        object_owner = getattr(self.get_object(), 'autor')

        if current_user != object_owner:
            return redirect('tiendas:tiendas_list')
        return super(OwnershipMixin, self).dispatch(request, *args, **kwargs)

@login_required(login_url='/')
def tiendas_list(request):
    tiendas_disp = Tienda.objects.filter(estado='APROBADA')
    tiendas_pers = Tienda.objects.filter(autor=request.user, estado='PENDIENTE')
    context = {'tiendas_disp':tiendas_disp, 'tiendas_pers':tiendas_pers}
    
    return render(request, 'tiendas/tiendas_list.html', context)

class TiendasList(ListView):                        
    model = Tienda
    template_name = 'tiendas/tiendas_list.html'
    queryset = Tienda.objects.all()
    paginate_by = 10

class TiendasCreate(CreateView):
    model = Tienda
    form_class = TiendaForm
    template_name = 'tiendas/tiendas_form.html'
    success_url = reverse_lazy('tiendas:tiendas_list')

    def get_success_url(self):
        next = self.request.GET.get('next', '')
        id = self.request.GET.get('id', '0')
        if next == 'productos':
            if id != '0':
                self.success_url = reverse_lazy('productos:producto_update', args=[id])
            else:
                self.success_url = reverse_lazy('productos:producto_form')   
        return self.success_url
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super(TiendasCreate, self).form_valid(form)

class TiendasUpdate(OwnershipMixin, UpdateView):
    model = Tienda
    form_class = TiendaForm
    template_name = 'tiendas/tiendas_form.html'
    success_url = reverse_lazy('tiendas:tiendas_list')

    def get_success_url(self):
        next = self.request.GET.get('next', '')
        id = self.request.GET.get('id', '0')
        if next == 'productos':
            self.success_url = reverse_lazy('productos:producto_form', args=[id])   
        return self.success_url

class TiendasDelete(OwnershipMixin, DeleteView):
    model = Tienda
    template_name = 'tiendas/tiendas_delete.html'
    success_url = reverse_lazy('tiendas:tiendas_list')

