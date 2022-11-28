from django.contrib import admin
from .models import Zamowienia, Faktury, Szczegoly_zamowienia

admin.site.register(Zamowienia)
admin.site.register(Faktury)
admin.site.register(Szczegoly_zamowienia)