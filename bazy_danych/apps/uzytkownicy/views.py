from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import UpdateView
from .forms import UserChangeForm, UserCreationForm, ContactCreationEditForm 
from django.shortcuts import render
from .models import Kontakty, Adresy, Uzytkownicy
from ..produkty.models import Opinie


class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')


class UserEditView(UpdateView):
    form_class = UserChangeForm
    template_name = 'registration/registration.html'
    
    def get_queryset(self):
        breakpoint()
        return Uzytkownicy.objects.get(pk = self.request.user.pk)


@login_required
def edit_contact(request):
    contact, _ = Kontakty.objects.get_or_create(
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

@login_required
def edit_address(request):
    address, _ = Adresy.objects.get_or_create(
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

@login_required
def user_opinions(request):
    opinions = Opinie.objects.filter(id_uzytkownika=request.user.pk)
    context = {'opinions': opinions}
    return render(request, 'userOpinionsList.html', context)


class UserOpinionUpdateView(LoginRequiredMixin, UpdateView):
    model = Opinie
    fields = ['tresc']
    template_name = 'opinionUpdate.html'
    success_url = reverse_lazy('home')