# Generated by Django 4.1 on 2022-09-15 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_hotel', '0005_delete_invoices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galery',
            name='hotel_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='my_hotel.hotels', verbose_name='Отель'),
        ),
    ]