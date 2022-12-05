from django.views import generic
from .forms import UserChangeForm, UserCreationForm


class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration.html'
    # success_url = reverse_lazy('login')       # move to login page ('login' its name in urls.py)