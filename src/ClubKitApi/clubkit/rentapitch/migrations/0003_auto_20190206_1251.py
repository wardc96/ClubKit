# Generated by Django 2.1 on 2019-02-06 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentapitch', '0002_auto_20190202_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentpitch',
            name='pitch_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pitches', to='clubs.Pitch'),
        ),
    ]