# Generated by Django 2.1.5 on 2019-02-10 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0015_auto_20190206_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubpackages',
            name='player_register_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clubpackages',
            name='rent_a_pitch_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clubpackages',
            name='roster_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clubpackages',
            name='shop_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
            preserve_default=False,
        ),
    ]
