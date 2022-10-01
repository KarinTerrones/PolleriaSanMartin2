from django import forms
from django.forms import ModelForm
from documento.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(max_length=80)

    class Meta:
        model = Account
        fields = ['email','username','password1','password2']

class LoginForm(forms.ModelForm):

    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    
    class  Meta:
        model = Account
        fields = {'email','password'}
    def clean(self):
        email= self.cleaned_data['email']
        password=self.cleaned_data['password']
        if not authenticate(email=email,password=password):
            raise forms.ValidationError('Login Invalido')


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
        fields = ["nombre","apellido_pater","apellido_mater","celular","foto_perfil"]
        widgets = {
            "nombre" : forms.TextInput(attrs={'class':'form-control'}),
            "apellido_pater" : forms.TextInput(attrs={'class':'form-control'}),
            "apellido_mater" : forms.TextInput(attrs={'class':'form-control'}),
            "celular" : forms.TextInput(attrs={'class':'form-control'}),
            "foto_perfil" : forms.FileInput(attrs={'class':'form-control'}),
        }
        labels = {
            "nombre" : "Nombre",
            "apellido_pater":"Apellido Paterno",
            "apellido_mater" :"Apellido Materno",
            "celular" : "Celular",
            "foto_perfil" : "Foto de Perfil",

        }

