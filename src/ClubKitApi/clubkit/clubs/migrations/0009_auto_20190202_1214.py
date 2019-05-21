# Generated by Django 2.1 on 2019-02-02 12:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0008_auto_20190202_1200'),
    ]

    operations = [

        migrations.AlterField(
            model_name='pitch',
            name='rental_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]