from django.urls import path, include
from .views import editContact

urlpatterns = [
    path('kontakt/', editContact, name='kontakt')
]
