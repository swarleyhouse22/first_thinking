from django.db import models
from django.contrib.auth import get_user_model
from django import forms

import json

# Create your models here.

LISTA_ESTADOS = (
    ('Pendiente','pendiente'),
    ('Terminada','terminada'),
)


class Lista(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    costoTotalReal = models.IntegerField(default=0)
    costoTotalPresupuestado = models.IntegerField()
    estado = models.CharField(max_length=20, choices=LISTA_ESTADOS, default='Pendiente')
    productos = models.ManyToManyField('productos.Producto')
    usuario = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    @property
    def json(self):
        return json.dumps(self)

    def __str__(self):
        return self.nombre