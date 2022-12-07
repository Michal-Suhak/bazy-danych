from django.urls import path
from .views import AllManufacturersView, ManufacturerCreateView


urlpatterns = [
    path('dodaj-producenta/', ManufacturerCreateView.as_view(), name='dodaj-producenta'),
    path('lista-producentow/', AllManufacturersView.as_view(), name='lista-producentow')
]
