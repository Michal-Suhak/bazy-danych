# Generated by Django 3.2.12 on 2022-12-11 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produkty', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produkty',
            name='zdjecie',
        ),
    ]
