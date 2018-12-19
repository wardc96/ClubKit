# Generated by Django 2.1 on 2018-12-19 13:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(default='', max_length=50)),
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
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfileInfo',
        ),
    ]
