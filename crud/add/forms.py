from dataclasses import fields
from tkinter import Widget
from django.core import validators
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
     model = User
     fields = ['name', 'email', 'mobile']
     widgets = {
         'name': forms.TextInput(attrs={'class':'form-control'}),
         'email': forms.EmailInput(attrs={'class':'form-control'}),
         'mobile': forms.TextInput(attrs={'class':'form-control'})
         ,
     }
     