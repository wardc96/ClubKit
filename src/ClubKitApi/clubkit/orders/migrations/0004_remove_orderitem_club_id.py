# Generated by Django 2.1.5 on 2019-05-22 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_orderitem_club_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='club_id',
        ),
    ]
