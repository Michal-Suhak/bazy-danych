from django.urls import path
from .views import (AllManufacturersView, ManufacturerCreateView, AllProductsView, AllCategoriesView,
                    CategoryCreateView, products_details, add_product, CategoryUpdateView, CategoryDeleteView,
                    ManufacturerUpdateView, ManufacturerDeleteView)


urlpatterns = [
    path('dodaj-producenta/', ManufacturerCreateView.as_view(), name='dodaj-producenta'),
    path('lista-producentow/', AllManufacturersView.as_view(), name='lista-producentow'),
    path('producent/<int:pk>/edytuj/', ManufacturerUpdateView.as_view(), name='edytuj-producenta'),
    path('producent/<int:pk>/usun/', ManufacturerDeleteView.as_view(), name='usun-producenta'),
    path('dodaj-produkt/', add_product, name='dodaj-produkt'),
    path('lista-produktow/', AllProductsView.as_view(), name='lista-produktow'),
    path('lista-kategorii/', AllCategoriesView.as_view(), name='lista-kategorii'),
    path('dodaj-kategorie/', CategoryCreateView.as_view(), name='dodaj-kategorie'),
    path('kategoria/<int:pk>/edytuj/', CategoryUpdateView.as_view(), name='edytuj-kategorie'),
    path('kategoria/<int:pk>/usun/', CategoryDeleteView.as_view(), name='usun-kategorie'),
    path('<int:pk>/detale/', products_details, name='detale-produktu')
]
