from django.db import models
from clubkit.clubs.models import ClubInfo, ClubMemberships


# Model to store player information to be used for membership registration
class Player(models.Model):

    club_id = models.ForeignKey(ClubInfo, on_delete=models.CASCADE)
    membership_title = models.ForeignKey(ClubMemberships, on_delete=models.CASCADE)
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








