from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Uzytkownicy, Kontakty, Adresy


class UserCreationForm(UserCreationForm):
    class Meta:
        model = Uzytkownicy
        fields = ('email', 'imie', 'nazwisko')
        widgets = {
            'email': forms.TextInput(attrs={'class': 'email_input'}),
            'imie': forms.TextInput(attrs={'class': 'imie_input'}),
            'nazwisko': forms.TextInput(attrs={'class': 'nazwisko_input'})
        }


class UserChangeForm(forms.ModelForm):

    class Meta:
        model = Uzytkownicy
        fields = ('email', 'imie', 'nazwisko')
        widgets = {
            'email': forms.TextInput(attrs={'class': 'email_input'}),
            'imie': forms.TextInput(attrs={'class': 'imie_input'}),
            'nazwisko': forms.TextInput(attrs={'class': 'nazwisko_input'})
        }


class ContactCreationEditForm(forms.ModelForm):

    class Meta:
        model = Kontakty
        fields = {'telefon', 'email'}
        widgets = {
            'telefon': forms.TextInput(attrs={'class': 'phone_input'}),
            'email': forms.EmailInput(attrs={'class': 'email_input'})
        }