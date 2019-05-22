from django.db import models
from clubkit.clubs.models import ClubInfo, Pitch


# Model to store pitch rental information to be used for rental purposes
class RentPitch(models.Model):
    club_id = models.ForeignKey(ClubInfo, on_delete=models.CASCADE)
    pitch_id = models.ForeignKey(Pitch, on_delete=models.CASCADE, related_name="pitches")
    rental_cost = models.DecimalField(max_digits=6, decimal_places=2, blank=True, default=0)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    mobile = models.CharField(max_length=15)
    date = models.DateField(null=False)
    start_time = models.TimeField(null=False)
    finish_time = models.TimeField(null=False)
    PAYMENT_TYPE = (
        ('1', 'Card'),
        ('2', 'Cash'),
    )
    payment_type = models.CharField(max_length=1, choices=PAYMENT_TYPE, blank=True)
    CANCEL_TYPE = (
        ('0', 'No'),
        ('1', 'Yes'),
    )
    is_cancelled = models.CharField(max_length=1, choices=CANCEL_TYPE, blank=True)

