# Generated by Django 4.1 on 2022-08-19 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_hotel', '0006_alter_tag_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_user', models.CharField(max_length=30, verbose_name='Имя')),
                ('email_user', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
            ],
        ),
    ]
