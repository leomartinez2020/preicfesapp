from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import Municipio, Departamento

class MunicipioForm(ModelForm):
    #municipio = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'required': True, 'placeholder': 'Buscar'}))
    class Meta:
        model = Municipio
        fields = ['nombre', 'departamento']
        labels = {
            'nombre': _('Municipio'),
        }


class DepartamentoForm2(ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre']
        labels = {
            'nombre': _('Departamento'),
        }


class DepartamentoForm(forms.Form):
    departamento = forms.ModelChoiceField(queryset=Departamento.objects.all())
    municipio = forms.ChoiceField(choices='')
