# Generated by Django 2.1 on 2019-02-02 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0010_auto_20190202_1217'),
        ('rentapitch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentpitch',
            name='club_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='clubs.ClubInfo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rentpitch',
            name='rental_cost',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]