from django.urls import path
from .views import AllInvoicesView, overall_order

urlpatterns = [
    path('faktury/', AllInvoicesView.as_view(), name='faktury'),
    path('zamowienie/', overall_order, name='zamowienie')
]
