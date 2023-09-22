from .models import *
from django import forms
class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ("name","email", "phone")
from django.forms.models import ModelForm
