from django.db import models
from clubkit.clubs.models import ClubInfo, Pitch, Team


class RosterId(models.Model):
    club_id = models.ForeignKey(ClubInfo, on_delete=models.CASCADE)
    pitch_id = models.ForeignKey(Pitch, on_delete=models.CASCADE)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)
    date = models.DateField(max_length=8)
    start_time = models.TimeField(default='')
    finish_time = models.TimeField(default='')
    reoccuring_event = models.BooleanField(default=False)

    def __str__(self):
        return "%s %s" % (self.pitch_name, self.team_name)












