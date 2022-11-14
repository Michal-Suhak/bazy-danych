from django.db import models
from użytkownicy.models import Użytkownicy
from produkty.models import Produkty

class Zamowienia:
    ilosc = models.IntegerField()


class Sczegoly_zamowienia:
    id_zamowienia = models.ForeignKey(Zamowienia, on_delete=models.PROTECT)
    id_produktu = models.ForeignKey(Produkty, on_delete=models.PROTECT)

class Faktury:
    id_użytkownika = models.ForeignKey(Użytkownicy, on_delete=models.PROTECT)
    id_zamowienia = models.ForeignKey(Sczegoly_zamowienia, on_delete=models.PROTECT)
    kwota = models.DecimalField(decimal_places=2)
    data_wystawienia = models.DateField(auto_created=True)