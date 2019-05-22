# Generated by Django 2.1.5 on 2019-05-21 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player_register', '0003_player_membership_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
    ]