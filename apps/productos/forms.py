from .models import Producto
from django import forms

from apps.tiendas.models import Tienda


class ProductosForm(forms.ModelForm):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tienda'].queryset = (Tienda.objects.filter(estado="APROBADA") | Tienda.objects.filter(autor=request.user)).distinct()
    
    class Meta:
        model=Producto
        fields = [
            'nombre',
            'costoPresupuestado',
            'costoReal',
            'estado',
            'notas',
            'tienda'
        ]
        labels = {
            'nombre':'Nombre',
            'costoPresupuestado':'Costo Presupuestado',
            'costoReal':'Costo Real',
            'estado':'Estado',
            'notas':'Notas',
            'tienda':'Tienda'
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'costoPresupuestado':forms.TextInput(attrs={'class':'form-control'}),
            'costoReal':forms.TextInput(attrs={'class':'form-control'}),
            'estado':forms.Select(choices="PRODUCTO_ESTADOS",attrs={'class':'form-control'}),
            'notas':forms.TextInput(attrs={'class':'form-control'}),
            'tienda':forms.Select(attrs={'class':'form-control'})
        }