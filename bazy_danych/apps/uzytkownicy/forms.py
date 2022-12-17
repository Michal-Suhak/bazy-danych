from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Uzytkownicy, Kontakty, Adresy


class UserCreationForm(UserCreationForm):
    class Meta:
        model = Uzytkownicy
        fields = ('email', 'imie', 'nazwisko')
        widgets = {
            'email': forms.TextInput(attrs={'class': 'email_input form-control'}),
            'imie': forms.TextInput(attrs={'class': 'imie_input form-control'}),
            'nazwisko': forms.TextInput(attrs={'class': 'nazwisko_input form-control'})
        }


class UserChangeForm(forms.ModelForm):

    class Meta:
        model = Uzytkownicy
        fields = ('email', 'imie', 'nazwisko')
        widgets = {
            'email': forms.TextInput(attrs={'class': 'email_input form-control'}),
            'imie': forms.TextInput(attrs={'class': 'imie_input form-control'}),
            'nazwisko': forms.TextInput(attrs={'class': 'nazwisko_input form-control'})
        }


class ContactCreationEditForm(forms.ModelForm):

    class Meta:
        model = Kontakty
        fields = {'telefon', 'email'}
        widgets = {
            'telefon': forms.TextInput(attrs={'class': 'phone_input form-control'}),
            'email': forms.EmailInput(attrs={'class': 'email_input form-control'})
        }