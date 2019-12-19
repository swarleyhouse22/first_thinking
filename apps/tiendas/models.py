from django.db import models
from django.contrib.auth.models import User
from django import forms


# Create your models here.

OPCIONES_ESTADO = (
    ('PENDIENTE', 'Pendiente'),
    ('APROBADA', 'Aprobada'),
)

class Tienda(models.Model):
    
    nombreTienda = models.CharField(max_length=50)
    nombreSucursal = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    estado = models.CharField(max_length=20, default="PENDIENTE", choices=OPCIONES_ESTADO)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreTienda + " - " + self.nombreSucursal

    class Meta:
        unique_together = ('nombreTienda', 'nombreSucursal', 'direccion', 'ciudad', 'region')


class TiendaForm(forms.ModelForm):

    class Meta:
        model = Tienda
        fields = [
            'nombreTienda',
            'nombreSucursal',
            'direccion',
            'ciudad',
            'region'
        ]
        labels = {
            'nombreTienda': "Nombre",
            'nombreSucursal': "Nombre de Sucursal",
            'direccion': "Dirección",
            'ciudad': "Ciudad",
            'region': "Región"
        }
        widgets = {
            'nombreTienda':forms.TextInput(attrs={'class':'form-control'}),
            'nombreSucursal':forms.TextInput(attrs={'class':'form-control'}),
            'direccion':forms.TextInput(attrs={'class':'form-control'}),
            'ciudad':forms.TextInput(attrs={'class':'form-control'}),
            'region':forms.TextInput(attrs={'class':'form-control'}),
        }
        error_messages = {
            '__all__': {
                'unique_together': 'La sucursal de la tienda que intentas agregar ya existe.',
            }
        }

