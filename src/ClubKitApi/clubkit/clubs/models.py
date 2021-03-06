from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from uuslug import slugify
from django.urls import reverse


# Model to store club information that will be displayed on club home page
class ClubInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    club_name = models.CharField(max_length=50, default='', unique=True)
    description = models.CharField(max_length=100)
    club_logo = models.ImageField(upload_to='profile_pics', blank=True)
    club_address1 = models.CharField(max_length=30)
    club_address2 = models.CharField(max_length=30, default='')
    club_address3 = models.CharField(max_length=30, default='')
    club_town = models.CharField(max_length=30)
    club_county = models.CharField(max_length=30)
    club_country = models.CharField(max_length=30)
    paypal_id = models.CharField(max_length=30)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.club_name


# Model to store club information on what clubs have access to what packages
class ClubPackages(models.Model):
    club_id = models.ForeignKey(ClubInfo, on_delete=models.CASCADE)
    PACKAGE_STATUS = (
        ('0', 'Active'),
        ('1', 'Not Active')
    )
    player_register_package = models.CharField(default='1', max_length=1, choices=PACKAGE_STATUS)
    player_register_price = models.DecimalField(default=100.00, max_digits=8, decimal_places=2)
    player_register_expiry = models.DateField(default=timezone.now)
    roster_package = models.CharField(default='1', max_length=1, choices=PACKAGE_STATUS)
    roster_price = models.DecimalField(default=50.00, max_digits=8, decimal_places=2)
    roster_expiry = models.DateField(default=timezone.now)
    rent_a_pitch_package = models.CharField(default='1', max_length=1, choices=PACKAGE_STATUS)
    rent_a_pitch_price = models.DecimalField(default=100.00, max_digits=8, decimal_places=2)
    rent_a_pitch_expiry = models.DateField(default=timezone.now)
    shop_package = models.CharField(default='1', max_length=1, choices=PACKAGE_STATUS)
    shop_price = models.DecimalField(default=50.00, max_digits=8, decimal_places=2)
    shop_expiry = models.DateField(default=timezone.now)


# Model to store clubs available memberships so members can select and pay on registration page
class ClubMemberships(models.Model):

    club_id = models.ForeignKey(ClubInfo, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, default='')
    price = models.DecimalField(default=0.00, max_digits=6, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.title


# Model to store club information about their teams to be used in roster feature
class Team(models.Model):

    club_id = models.ForeignKey(ClubInfo, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='team_pics', blank=True)
    team_name = models.CharField(max_length=30)
    manager_name = models.CharField(max_length=20)

    def __str__(self):
        return self.team_name


# Model to store pitch information to be used for rental and roster purposes
class Pitch(models.Model):
    club_id = models.ForeignKey(ClubInfo, on_delete=models.CASCADE, related_name="pitches")
    pitch_name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='pitch_pics', blank=True)
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
    RENT_TYPE = (
        ('0', 'Not Available To Rent'),
        ('1', 'Available To Rent'),
    )
    rental = models.CharField(max_length=1, choices=RENT_TYPE)
    rental_price = models.DecimalField(default=0.00, max_digits=6, decimal_places=2)
    max_people = models.IntegerField(null=True)

    def __str__(self):
        return self.pitch_name


# Model to store club posts that will be displayed and added from the club home page
class ClubPosts(models.Model):
    club_id = models.ForeignKey(ClubInfo, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='club_post_pics', blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Packages(models.Model):
    club_id = models.ForeignKey(ClubInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('clubs:product_detail', args=[self.id, self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Packages, self).save(*args, **kwargs)








