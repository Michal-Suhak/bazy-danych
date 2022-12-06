from django.views import generic
from django.views.generic import UpdateView
from .forms import UserChangeForm, UserCreationForm, ContactCreationEditForm 
from django.shortcuts import render
from .models import Kontakty, Adresy

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration.html'
    # success_url = reverse_lazy('login')       # move to login page ('login' its name in urls.py)


class UserEditView(UpdateView):
    form_class = UserChangeForm
    template_name = ''


def editContact(request):
    contact, created = Kontakty.objects.get_or_create(
        id_uzytkownika = request.user
    )
    form = ContactCreationEditForm(request.POST)
    response = form.save(commit=False)
    print(response.email)
    if response.telefon or response.email:
        contact.telefon = response.telefon
        contact.email = response.email
    contact.save()

    context = {'form': contact}

    return render(request, 'contacts/editContact.html', context)