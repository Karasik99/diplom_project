# Generated by Django 4.1 on 2022-09-04 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_hotel', '0004_invoices'),
    ]

    operations = [
        migrations.DeleteModel(
            name='invoices',
        ),
    ]
