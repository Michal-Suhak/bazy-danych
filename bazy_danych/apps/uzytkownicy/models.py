from django.db import models


class Kontakty(models.Model):
    telefon = models.CharField(max_length=12, null=True, blank=True)
    email = models.CharField(max_length=50, blank=True, null=True)


class Adresy(models.Model):
    miejscowosc = models.CharField(max_length=70)
    powiat = models.CharField(max_length=50)
    wojewodztwo = models.CharField(max_length=50)
    kod_pocztowy = models.CharField(max_length=6)
    ulica = models.CharField(max_length=70, null=True, blank=True)
    numer_domu = models.IntegerField()
    numer_lokalu = models.IntegerField(null=True, blank=True)


class Uzytkownicy(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    id_kontaktu  = models.ForeignKey(Kontakty, on_delete=models.CASCADE)
    id_adresu = models.ForeignKey(Adresy, on_delete=models.CASCADE)
