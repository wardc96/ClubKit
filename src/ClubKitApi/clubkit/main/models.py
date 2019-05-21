from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Model to store our available packages
class OurPackages(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
            return self.title









