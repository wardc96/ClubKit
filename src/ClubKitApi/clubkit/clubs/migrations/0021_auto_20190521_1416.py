# Generated by Django 2.1.5 on 2019-05-21 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0020_clubinfo_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubinfo',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]
