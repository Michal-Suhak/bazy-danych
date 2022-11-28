from django.db import models
from apps.uzytkownicy.models import Uzytkownicy


class Producenci(models.Model):
    nazwa_producenta = models.CharField(max_length=100)


class Produkty(models.Model):
    nazwa = models.TextField(max_length=100)
    cena = models.DecimalField(decimal_places=2, max_digits=5)
    opis = models.TextField(max_length=255, null=True, blank=True)
    zdjecie = models.ImageField()
    id_producenta = models.ForeignKey(Producenci,on_delete=models.PROTECT)


class Kategorie(models.Model):
    nazwa_kategorii = models.CharField(max_length=70)


class Kategoria_produktu(models.Model):
    id_produktu = models.ForeignKey(Produkty, on_delete=models.PROTECT)
    id_kategorii = models.ForeignKey(Kategorie, on_delete=models.CASCADE)


class Opinie(models.Model):
    tresc = models.CharField(max_length=255)
    data_wystawienia = models.DateField(auto_created=True)
    id_uzytkownika = models.ForeignKey(Uzytkownicy, on_delete=models.CASCADE)
    id_produktu = models.ForeignKey(Produkty, on_delete=models.CASCADE)
    