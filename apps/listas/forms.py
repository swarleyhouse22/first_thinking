from .models import Lista
from django import forms


class ListaForm(forms.ModelForm):

    class Meta:
        model=Lista
        fields = [
            'nombre',
            'costoTotalPresupuestado',           
            'estado',          
        ]
        labels = {
            'nombre':'Nombre',
            'costoTotalPresupuestado':'Costo Total Presupuestado',
            'estado':'Estado',            
        }
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'costoTotalPresupuestado':forms.TextInput(attrs={'class':'form-control'}),
            'estado':forms.Select(choices="LISTA_ESTADOS",attrs={'class':'form-control'}),
        }