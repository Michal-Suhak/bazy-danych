from django import forms
from .models import Producenci


class ManufacturerForm(forms.ModelForm):

    class Meta:
        model = Producenci
        fields = {'nazwa_producenta'}
        widgets = {
            'nazwa_producenta': forms.Textarea(attrs={'class': 'manufacturer_name_field'})
        }