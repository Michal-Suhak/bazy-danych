from django.urls import path
from .views import (AllManufacturersView, ManufacturerCreateView, AllProductsView, ProductCreateView, AllCategoriesView,
 CategoryCreateView, make_order)


urlpatterns = [
    path('dodaj-producenta/', ManufacturerCreateView.as_view(), name='dodaj-producenta'),
    path('lista-producentow/', AllManufacturersView.as_view(), name='lista-producentow'),
    path('dodaj-produkt/', ProductCreateView.as_view(), name='dodaj-produkt'),
    path('lista-produktow/', AllProductsView.as_view(), name='lista-produktow'),
    path('lista-kategorii/', AllCategoriesView.as_view(), name='lista-kategorii'),
    path('dodaj-kategorie/', CategoryCreateView.as_view(), name='dodaj-kategorie'),
    path('<int:pk>/detale/', make_order, name='detale-produktu')
]
