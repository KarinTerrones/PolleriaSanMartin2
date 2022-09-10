from pyexpat import model
from tkinter import Widget
from django import forms
from django.forms import ModelForm
from documento.models import *

class DocumentoForm(forms.ModelForm):

    class Meta:
        model = Documento
        fields = ["nombre","tipo","proveedor","pedido"]
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'pedido' : forms.Textarea(attrs={'class':'form-control'}),
        }

class PerfilEncargado(forms.ModelForm):

    class Meta:
        model = EncargadoArea
        fields = ["email","nombre","apellido_pater","apellido_mater","celular","foto_perfil"]
        widgets = {
            "email" : forms.TextInput(attrs={'class':'form-control'}),
            "nombre" : forms.TextInput(attrs={'class':'form-control'}),
            "apellido_pater" : forms.TextInput(attrs={'class':'form-control'}),
            "apellido_mater" : forms.TextInput(attrs={'class':'form-control'}),
            "celular" : forms.TextInput(attrs={'class':'form-control'}),
            "foto_perfil" : forms.FileInput(attrs={'class':'form-control'}),
        }
        labels = {
            "email" : "Correo",
            "nombre" : "Nombre",
            "apellido_pater":"Apellido Paterno",
            "apellido_mater" :"Apellido Materno",
            "celular" : "Celular",
            "foto_perfil" : "Foto de Perfil",

        }

