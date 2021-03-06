# Generated by Django 2.1 on 2019-01-19 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(default='', max_length=50, unique=True)),
                ('club_logo', models.ImageField(blank=True, upload_to='profile_pics')),
                ('club_address1', models.CharField(max_length=30)),
                ('club_address2', models.CharField(default='', max_length=30)),
                ('club_address3', models.CharField(default='', max_length=30)),
                ('club_town', models.CharField(max_length=30)),
                ('club_county', models.CharField(max_length=30)),
                ('club_country', models.CharField(max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pitch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pitch_name', models.CharField(max_length=30)),
                ('pitch_size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1)),
                ('pitch_type', models.CharField(choices=[('1', 'Outdoor'), ('2', 'Indoor')], max_length=1)),
                ('open_time', models.TimeField(default='09:00')),
                ('close_time', models.TimeField(default='22:00')),
                ('club_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pitches', to='clubs.ClubInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=30)),
                ('manager_name', models.CharField(max_length=20)),
                ('club_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clubs.ClubInfo')),
            ],
        ),
    ]
