from django.db import models
from clubkit.clubs.models import ClubInfo, Pitch


# Model to store pitch rental information to be used for rental purposes
class RentPitch(models.Model):
    club_id = models.ForeignKey(ClubInfo, on_delete=models.CASCADE)
    pitch_id = models.ForeignKey(Pitch, on_delete=models.CASCADE, related_name="pitches")
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile = models.CharField(max_length=15)
    date = models.DateField(null=False)
    start_time = models.TimeField(null=False)
    finish_time = models.TimeField(null=False)


