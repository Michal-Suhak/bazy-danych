from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Producenci
from .forms import ManufacturerForm


class AllManufacturersView(ListView):
    model = Producenci
    template_name = 'manufacturer/manufacturersList.html'
    ordering = ['-id']


class ManufacturerCreateView(CreateView):
    model = Producenci
    template_name = 'manufacturer/manufacturerAdd.html'
    form_class = ManufacturerForm
    success_url = reverse_lazy('lista-producentow')