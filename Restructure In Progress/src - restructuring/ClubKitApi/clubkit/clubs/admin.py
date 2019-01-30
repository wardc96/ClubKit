from django.contrib import admin
from clubkit.clubs.models import ClubInfo, Team, Pitch, ClubPosts, ClubPackages, ClubMemberships


# Register your models here.
admin.site.register(ClubInfo)
admin.site.register(Team)
admin.site.register(Pitch)
admin.site.register(ClubPosts)
admin.site.register(ClubPackages)
admin.site.register(ClubMemberships)
