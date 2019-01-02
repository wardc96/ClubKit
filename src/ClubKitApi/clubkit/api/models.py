from django.db import models
from django.contrib.auth.models import User
from clubkit.api.utils import unique_slug_generator
from django.db.models.signals import pre_save


# Club information model


class ClubInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    club_name = models.CharField(max_length=50, default='')
    club_logo = models.ImageField(upload_to='profile_pics', blank=True)
    club_address1 = models.CharField(max_length=30)
    club_address2 = models.CharField(max_length=30, default='')
    club_address3 = models.CharField(max_length=30, default='')
    club_town = models.CharField(max_length=30)
    club_county = models.CharField(max_length=30)
    club_country = models.CharField(max_length=30)
    # slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.club_name


'''
link to video: https://www.youtube.com/watch?v=bQHqG-LMWPY
def slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.club_name, instance.slug)

pre_save.connect(slug_save, sender=ClubInfo)
'''


class PlayerRegistration(models.Model):

    club_name = models.ForeignKey(ClubInfo, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    dob = models.DateField(max_length=8)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=12)
    mobile = models.CharField(max_length=15)
    emergency_contact_name = models.CharField(max_length=40)
    emergency_contact_mobile = models.CharField(max_length=15)
    address1 = models.CharField(max_length=30)
    address2 = models.CharField(max_length=30, default='')
    address3 = models.CharField(max_length=30, default='')
    town = models.CharField(max_length=30)
    county = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

