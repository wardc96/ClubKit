from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# from clubkit.player_register.models import Player


# Club information model

class ClubInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    club_name = models.CharField(max_length=50, default='', unique=True)
    club_logo = models.ImageField(upload_to='profile_pics', blank=True)
    club_address1 = models.CharField(max_length=30)
    club_address2 = models.CharField(max_length=30, default='')
    club_address3 = models.CharField(max_length=30, default='')
    club_town = models.CharField(max_length=30)
    club_county = models.CharField(max_length=30)
    club_country = models.CharField(max_length=30)

    def __str__(self):
        return self.club_name


class Team(models.Model):

    club_id = models.ForeignKey(ClubInfo, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=30)
    manager_name = models.CharField(max_length=20)
    # player_id = models.ManyToManyField(Player, on_delete=models.CASCADE)

    def __str__(self):
        return self.team_name


class Pitch(models.Model):
    club_id = models.ForeignKey(ClubInfo, on_delete=models.CASCADE, related_name="pitches")
    pitch_name = models.CharField(max_length=30)
    PITCH_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    PITCH_TYPE = (
        ('1', 'Outdoor'),
        ('2', 'Indoor'),
    )
    pitch_size = models.CharField(max_length=1, choices=PITCH_SIZES)
    pitch_type = models.CharField(max_length=1, choices=PITCH_TYPE)
    open_time = models.TimeField(default='09:00')
    close_time = models.TimeField(default='22:00')

    def __str__(self):
        return self.pitch_name












