from django.db import models
from clubkit.clubs.models import ClubInfo, Pitch, Team


# Model to store roster information
class RosterId(models.Model):
    club_id = models.ForeignKey(ClubInfo, on_delete=models.CASCADE)
    pitch_id = models.ForeignKey(Pitch, on_delete=models.CASCADE)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    date = models.DateField(max_length=8)
    start_time = models.TimeField(default='')
    finish_time = models.TimeField(default='')
    reoccuring_event = models.BooleanField(default=False)
    DAYS = (
        ('1', 'Monday'),
        ('2', 'Tuesday'),
        ('3', 'Wednesday'),
        ('4', 'Thursday'),
        ('5', 'Friday'),
        ('6', 'Saturday'),
        ('7', 'Sunday'),
    )
    reoccuring_day = models.CharField(max_length=1, choices=DAYS, blank=True, null=True)









