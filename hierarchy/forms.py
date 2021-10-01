from django import forms
from hierarchy.models import Hierarchy
from django.forms.fields import CharField
from django.forms.widgets import PasswordInput

class MyFilesForm(forms.Form):
    name = forms.CharField(max_length=200)
    parent = forms.ModelChoiceField(queryset=Hierarchy.objects.all(), required=False)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)