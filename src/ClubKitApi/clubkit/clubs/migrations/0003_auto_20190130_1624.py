# Generated by Django 2.1 on 2019-01-30 16:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0002_clubpackages_clubposts'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubpackages',
            name='player_register_expiry',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='clubpackages',
            name='rent_a_pitch_expiry',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='clubpackages',
            name='roster_expiry',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='clubpackages',
            name='shop_expiry',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
