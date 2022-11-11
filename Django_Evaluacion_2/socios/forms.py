from dataclasses import field, fields
from pyexpat import model
from django import forms 
from socios.models import Socio

class FormSocio(forms.ModelForm):
    nombresocio=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el nombre del socio'}))
    fechaincorporacion=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingrese el Fecha incorporacion'}))
    añodenacimiento=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingrese años nacimiento'}))
    telefono=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingrese telefono'}))
    correoelectronico=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Ingrese correo electronico'}))
    sexo=forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el sexo'}))
    class Meta: 
        model=Socio
        fields='__all__'

    
    