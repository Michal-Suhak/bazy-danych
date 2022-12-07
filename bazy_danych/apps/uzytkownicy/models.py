from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager


class Uzytkownicy(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True)
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    admin = models.BooleanField()
    staff = models.BooleanField()

    REQUIRED_FIELDS = ['imie', 'nazwisko']
    USERNAME_FIELD = 'email' 

    objects = UserManager()

    def get_full_name(self):
        return "{} {}".format(self.imie, self.nazwisko)

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """
            Does the user have a specific permission?
        """
        return True

    def has_module_perms(self, app_label):
        """
            Does the user have permissions to view the apps (the app_label)?
        """
        return True

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        return self.staff


class Kontakty(models.Model):
    id_uzytkownika  = models.OneToOneField(Uzytkownicy, on_delete=models.CASCADE, null=True)
    telefon = models.CharField(max_length=12, null=True, blank=True)
    email = models.CharField(max_length=50, blank=True, null=True)


class Adresy(models.Model):
    id_uzytkownika = models.OneToOneField(Uzytkownicy, on_delete=models.CASCADE, null=True)
    miejscowosc = models.CharField(max_length=70, blank=True)
    powiat = models.CharField(max_length=50, blank=True)
    wojewodztwo = models.CharField(max_length=50, blank=True)
    kod_pocztowy = models.CharField(max_length=6, blank=True)
    ulica = models.CharField(max_length=70, null=True, blank=True)
    numer_domu = models.IntegerField(null=True, blank=True)
    numer_lokalu = models.IntegerField(null=True, blank=True)