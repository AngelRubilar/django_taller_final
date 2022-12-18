from dataclasses import fields
from django import forms
from seminario.models import Seminario

class FormSeminario(forms.ModelForm):
    class Meta:
        model = Seminario
        fields = '__all__'