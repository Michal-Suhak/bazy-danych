from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import UpdateView
from .forms import UserChangeForm, UserCreationForm, ContactCreationEditForm 
from django.shortcuts import render
from .models import Kontakty, Adresy

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')       # move to login page ('login' its name in urls.py)


class UserEditView(UpdateView):
    form_class = UserChangeForm
    template_name = ''


def edit_contact(request):
    contact, created = Kontakty.objects.get_or_create(
        id_uzytkownika = request.user
    )
    response = ContactCreationEditForm(request.POST).save(commit=False)
    form_values = list(response.__dict__.values())
    for ind in range(1, len(form_values)):
        if form_values[ind] != None:
            contact.telefon = response.telefon
            contact.email = response.email
    contact.save()

    context = {'contact': contact}

    return render(request, 'editContact.html', context)

def edit_address(request):
    address, created = Adresy.objects.get_or_create(
        id_uzytkownika = request.user
    )
    response = ContactCreationEditForm(request.POST).save(commit=False)
    form_values = list(response.__dict__.values())
    for ind in range(1, len(form_values)):
        if form_values[ind] != None:
            address.miejscowosc = response.miejscowosc
            address.powiat = response.powiat
            address.wojewodztwo = response.wojewodztwo
            address.kod_pocztowy = response.kod_pocztowy
            address.ulica = response.ulica
            address.numer_domu = response.numer_dommu
            address.numer_lokalu = response.numer_lokalu
    address.save()

    context = {'address': address}

    return render(request, 'editAddress.html', context)