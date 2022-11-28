from django.contrib import admin
from .models import Producenci, Produkty, Kategorie, Opinie

admin.site.register(Produkty)
admin.site.register(Producenci)
admin.site.register(Kategorie)
admin.site.register(Opinie)
