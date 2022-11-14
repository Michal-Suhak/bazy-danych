from django.db import models
from użytkownicy.models import Użytkownicy

class Producenci:
    nazwa_producenta = models.CharField(max_length=100)


class Kategorie:
    nazwa_kategorii = models.CharField(max_length=70)


class Kategoria_produktu:
    id_producenta = models.ForeignKey(Producenci, on_delete=models.CASCADE)
    id_kategorii = models.ManyToManyField(Kategorie)


class Produkty:
    nazwa = models.TextField(max_length=100)
    cena = models.DecimalField(decimal_places=2)
    opis = models.TextField(max_length=255, null=True, blank=True)
    zdjecie = models.ImageField()
    id_kategorii = models.ForeignKey(Kategoria_produktu, on_delete=models.CASCADE)


class Opinie:
    tresc = models.CharField(max_length=255)
    data_wystawienia = models.DateField(auto_created=True)
    id_użytkownika = models.ForeignKey(Użytkownicy, on_delete=models.CASCADE)
    id_produktu = models.OneToOneField(Produkty)