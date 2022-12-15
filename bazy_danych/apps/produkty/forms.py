from django import forms
from .models import Producenci, Produkty, Kategorie, Opinie


class ManufacturerForm(forms.ModelForm):

    class Meta:
        model = Producenci
        fields = {'nazwa_producenta'}
        widgets = {
            'nazwa_producenta': forms.Textarea(attrs={'class': 'manufacturer_name_field'})
        }


class ProductForm(forms.ModelForm):

    class Meta:
        model = Produkty
        fields = {'nazwa', 'cena', 'opis', 'id_producenta'}
        widgets = {
            'nazwa': forms.Textarea(attrs={'class': 'product_name_field'})
        }


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Kategorie
        fields = {'nazwa_kategorii'}



class OpinionForm(forms.ModelForm):

    class Meta:
        model = Opinie
        fields = {'tresc'}