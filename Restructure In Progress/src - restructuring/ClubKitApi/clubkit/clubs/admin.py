from django.contrib import admin
from clubkit.clubs.models import ClubInfo, Team, Pitch


# Register your models here.
admin.site.register(ClubInfo)
admin.site.register(Team)
admin.site.register(Pitch)
