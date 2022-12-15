from datetime import date
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .decorators import StaffRequiredMixin, staff_required
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


class ManufacturerUpdateView(StaffRequiredMixin, UpdateView):
    model = Producenci
    fields = '__all__'
    template_name = 'manufacturer/manufacturerUpdate.html'
    success_url = reverse_lazy('lista-producentow')


class ManufacturerDeleteView(StaffRequiredMixin, DeleteView):
    model = Producenci
    fields = '__all__'
    template_name = 'manufacturer/manufacturerDelete.html'
    success_url = reverse_lazy('lista-producentow')


class AllProductsView(ListView):
    model = Produkty
    template_name = 'product/productList.html'
    ordering = ['-id']

    
@staff_required
def add_product(request):
    form = ProductForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'product/productAdd.html', context)


def products_details(request, pk):
    object = Produkty.objects.get(id=pk)
    ordered = False

    if request.method == 'POST' and "DELETE" in request.POST:
        object.id_producenta = None
        object.delete()
        return redirect('home')


    if request.method == 'POST' and "ADD" in request.POST:
        date_now = date.today()
        zamowienie, _ = Zamowienia.objects.get_or_create(
            id_uzytkownika = request.user,
            data_zamowienia = date_now,
            zakonczone = False
        )
        print(zamowienie)
        Szczegoly_zamowienia.objects.create(
            ilosc=request.POST['quantity'],
            id_zamowienia=zamowienie,
            id_produktu=object
        )
        ordered = True
    context = {'product': object, 'ordered': ordered}
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


class CategoryUpdateView(StaffRequiredMixin, UpdateView):
    model = Kategorie
    fields = '__all__'
    template_name = 'categories/categoryUpdate.html'
    success_url = reverse_lazy('lista-kategorii')


class CategoryDeleteView(StaffRequiredMixin, DeleteView):
    model = Kategorie
    fields = '__all__'
    template_name = 'categories/categoryDelete.html'
    success_url = reverse_lazy('lista-kategorii')