from django.urls import path, include
from .views import editContact, editAddress

urlpatterns = [
    path('kontakt/', editContact, name='kontakt'),
    path('adres/', editAddress, name='adres')
]
