from django.contrib import admin
from .models import Uzytkownicy, Kontakty, Adresy

admin.site.register(Kontakty)
admin.site.register(Adresy)

@admin.register(Uzytkownicy)
class Uzytkownicy(admin.ModelAdmin):
    list_display = ('email', 'imie', 'nazwisko')