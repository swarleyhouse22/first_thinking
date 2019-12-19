from django.db import models
from django.contrib.auth.models import User
from django import forms

import json
# Create your models here.

PRODUCTO_ESTADOS = (

   ('Listo', 'Listo'),
   ('Pendiente', 'Pendiente'),

)

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    costoPresupuestado = models.IntegerField()
    costoReal = models.IntegerField(default=0)
    tienda = models.ForeignKey('tiendas.Tienda', on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=PRODUCTO_ESTADOS, default='Pendiente')
    notas = models.CharField(max_length=50, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre 

    @property
    def json(self):
        return json.dumps(self)  

class ProductosForm(forms.ModelForm):

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
            'nombre':forms.TextInput(attrs={'class':'forms-control'}),
            'costoPresupuestado':forms.TextInput(attrs={'class':'forms-control'}),
            'costoReal':forms.TextInput(attrs={'class':'forms-control'}),
            'estado':forms.Select(choices="PRODUCTO_ESTADOS",attrs={'class':'forms-control'}),
            'notas':forms.TextInput(attrs={'class':'forms-control'}),
            'tienda':forms.Select(attrs={'class':'forms-control'}),
        }
