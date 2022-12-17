from django.urls import path
from .views import overall_order, all_invoices

urlpatterns = [
    path('faktury/', all_invoices, name='faktury'),
    path('zamowienie/', overall_order, name='zamowienie')
]
