from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def _create_user(self, email, password, imie, nazwisko, **extra_fields):
        """
            Creates and saves a User with a given eail, password and extra fields
        """
        if not email:
            raise ValueError("Nie podano emaila")
        email = self.normalize_email(email)
        user = self.model(
            email = email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_user(self, email, password, imie, nazwisko, **extra_fields):
        """
            Create and save a User with the given email and password

            :type email: str
            :type password: str
            :type extra_fields: dict
        """
        extra_fields.setdefault('admin', False)
        extra_fields.setdefault('staff', False)
        return self._create_user(email, password, imie, nazwisko, **extra_fields)

    def create_superuser(self, email, password, imie, nazwisko, **extra_fields):
        """
            Create and save a Super User with the given email and password

            :type email: str
            :type password: str
            :type extra_fields: dict
        """
        extra_fields.setdefault('admin', True)
        extra_fields.setdefault('staff', True)
        return self._create_user(email, password, imie, nazwisko, **extra_fields)