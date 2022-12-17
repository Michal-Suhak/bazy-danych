from django.urls import path, include
from .views import edit_contact, edit_address, user_opinions, UserOpinionUpdateView, UserEditView

urlpatterns = [
    path('kontakt/', edit_contact, name='kontakt'),
    path('adres/', edit_address, name='adres'),
    path('opinie-uzytkownika/', user_opinions, name='opinie-uzytkownika'),
    path('<int:pk>/edytuj-opinie-uzytkownika/', UserOpinionUpdateView.as_view(), name='edytuj-opinie-uzytkownika'),
    path('<int:pk>/edit/', UserEditView.as_view(), name="edytuj-uzytkownika")
]
