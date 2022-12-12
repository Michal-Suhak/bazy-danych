from django.db import models
from apps.uzytkownicy.models import Uzytkownicy
from apps.produkty.models import Produkty


class Zamowienia(models.Model):
    id_uzytkownika = models.ForeignKey(Uzytkownicy, on_delete=models.PROTECT, default=None)
    data_zamowienia = models.DateField(auto_created=True)
    zakonczone = models.BooleanField(default=False)


class Szczegoly_zamowienia(models.Model):
    ilosc = models.IntegerField()
    id_zamowienia = models.ForeignKey(Zamowienia, on_delete=models.PROTECT)
    id_produktu = models.ForeignKey(Produkty, on_delete=models.CASCADE)


class Faktury(models.Model):
    id_uzytkownika = models.ForeignKey(Uzytkownicy, on_delete=models.PROTECT)
    id_zamowienia = models.ForeignKey(Zamowienia, on_delete=models.PROTECT)
    kwota = models.DecimalField(decimal_places=2, max_digits=10)
    data_wystawienia = models.DateField(auto_created=True)
