from django.contrib import admin
from .models import Uzytkownicy, Kontakty, Adresy

admin.site.register(Kontakty)
admin.site.register(Adresy)
admin.site.register(Uzytkownicy)