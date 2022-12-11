# Generated by Django 3.2.12 on 2022-12-11 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zamowienia', '0002_zamowienia_zakonczone'),
    ]

    operations = [
        migrations.AddField(
            model_name='zamowienia',
            name='id_uzytkownika',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
