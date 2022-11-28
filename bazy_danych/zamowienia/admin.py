from django.contrib import admin
from .models import Zamowienia, Faktury, Sczegoly_zamowienia

admin.site.register(Zamowienia)
admin.site.register(Faktury)
admin.site.register(Sczegoly_zamowienia)