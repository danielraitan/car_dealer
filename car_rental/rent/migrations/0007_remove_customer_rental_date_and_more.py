# Generated by Django 4.1.4 on 2022-12-27 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0006_alter_carinfo_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='rental_date',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='return_date',
        ),
    ]
