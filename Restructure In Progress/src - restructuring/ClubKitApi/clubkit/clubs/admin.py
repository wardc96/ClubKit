from django.contrib import admin
from clubkit.clubs.models import ClubInfo, Team, Pitch, ClubPosts


# Register your models here.
admin.site.register(ClubInfo)
admin.site.register(Team)
admin.site.register(Pitch)
admin.site.register(ClubPosts)
