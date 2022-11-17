from django.db import models
from uzytkownicy.models import Uzytkownicy
from produkty.models import Produkty


class Zamowienia(models.Model):
    data_zamowienia = models.DateField(auto_created=True)


class Sczegoly_zamowienia(models.Model):
    ilosc = models.IntegerField()
    id_zamowienia = models.ForeignKey(Zamowienia, on_delete=models.PROTECT)
    id_produktu = models.ForeignKey(Produkty, on_delete=models.PROTECT)


class Faktury(models.Model):
    id_uzytkownika = models.ForeignKey(Uzytkownicy, on_delete=models.PROTECT)
    id_zamowienia = models.ForeignKey(Sczegoly_zamowienia, on_delete=models.PROTECT)
    kwota = models.DecimalField(decimal_places=2, max_digits=10)
    data_wystawienia = models.DateField(auto_created=True)
