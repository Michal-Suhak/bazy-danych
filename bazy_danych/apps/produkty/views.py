from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .decorators import StaffRequiredMixin
from .models import Producenci, Produkty, Kategorie
from .forms import ManufacturerForm, ProductForm, CategoryForm


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


class AllCategoriesView(StaffRequiredMixin, ListView):
    model = Kategorie
    template_name = 'categories/categoryList.html'
    ordering = ['-id']


class CategoryCreateView(StaffRequiredMixin, CreateView):
    model = Kategorie
    template_name = 'categories/categoryAdd.html'
    form_class = CategoryForm
    success_url = reverse_lazy('lista-kategorii')