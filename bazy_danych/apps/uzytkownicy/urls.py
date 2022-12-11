from django.urls import path, include
from .views import edit_contact, edit_address

urlpatterns = [
    path('kontakt/', edit_contact, name='kontakt'),
    path('adres/', edit_address, name='adres')
]
