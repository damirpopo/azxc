from django import forms
from django.forms import ModelForm


class crer(forms.Form):
    title = forms.CharField()
    subtile = forms.CharField()
    URL = forms.URLField()



    
