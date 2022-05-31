from django import forms
from django.forms import ModelForm
from evento_artistico import models

class productoresform(forms.Form):
    nombre = forms.CharField(max_length=40, label='nombre')
    apellido = forms.CharField(max_length=40, label='apellido')
    email = forms.EmailField(label='correo electronico')
    cuil = forms.IntegerField(label='CUIL')

class musicosform(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    instrumento = forms.CharField(max_length=40)
    cuil = forms.IntegerField()

class tecnicosform(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()
    cuil = forms.IntegerField()