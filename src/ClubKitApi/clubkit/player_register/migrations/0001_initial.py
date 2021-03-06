# Generated by Django 2.1 on 2019-01-19 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('dob', models.DateField(max_length=8)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('mobile', models.CharField(max_length=15)),
                ('emergency_contact_name', models.CharField(max_length=40)),
                ('emergency_contact_mobile', models.CharField(max_length=15)),
                ('address1', models.CharField(max_length=30)),
                ('address2', models.CharField(default='', max_length=30)),
                ('address3', models.CharField(default='', max_length=30)),
                ('town', models.CharField(max_length=30)),
                ('county', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
            ],
        ),
    ]
