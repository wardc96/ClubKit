from django.contrib import admin
from clubkit.api.models import ClubInfo, Player, Team, Pitch, RosterId

# Register your models here.
admin.site.register(ClubInfo)
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Pitch)
admin.site.register(RosterId)


