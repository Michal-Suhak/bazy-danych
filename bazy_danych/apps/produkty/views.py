from datetime import date
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from .decorators import StaffRequiredMixin
from .models import Producenci, Produkty, Kategorie
from .forms import ManufacturerForm, ProductForm, CategoryForm
from django.shortcuts import render, redirect

from apps.zamowienia.models import Zamowienia, Szczegoly_zamowienia


class AllManufacturersView(StaffRequiredMixin, ListView):
    model = Producenci
    template_name = 'manufacturer/manufacturersList.html'
    ordering = ['-id']


class ManufacturerCreateView(StaffRequiredMixin, CreateView):
    model = Producenci
    template_name = 'manufacturer/manufacturerAdd.html'
    form_class = ManufacturerForm
    success_url = reverse_lazy('lista-producentow')


class AllProductsView(ListView):
    model = Produkty
    template_name = 'product/productList.html'
    ordering = ['-id']


class ProductCreateView(StaffRequiredMixin, CreateView):
    model = Produkty
    template_name = 'product/productAdd.html'
    form_class = ProductForm
    success_url = reverse_lazy('lista-produktow')


# class ProductDetailsView(DetailView):
#     model = Produkty
#     template_name = 'product/productDetails.html'



def make_order(request, pk):
    item = Produkty.objects.get(id=pk)
    if request.method == 'POST':
        date_now = date.today()
        zamowienie, _ = Zamowienia.objects.get_or_create(
            id_uzytkownika = request.user,
            data_zamowienia = date_now
        )
        print(zamowienie)
        szczgoly_zamowienia = Szczegoly_zamowienia.objects.create(
            ilosc=request.POST['quantity'],
            id_zamowienia=zamowienie,
            id_produktu=item
        )
    object = Produkty.objects.get(id=pk)
    context = {'product': object}
    return render(request, 'product/productDetails.html', context)

class AllCategoriesView(StaffRequiredMixin, ListView):
    model = Kategorie
    template_name = 'categories/categoryList.html'
    ordering = ['-id']


class CategoryCreateView(StaffRequiredMixin, CreateView):
    model = Kategorie
    template_name = 'categories/categoryAdd.html'
    form_class = CategoryForm
    success_url = reverse_lazy('lista-kategorii')