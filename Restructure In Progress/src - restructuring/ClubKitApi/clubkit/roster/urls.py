from django.conf.urls import url
from clubkit.roster import views

# SET THE NAMESPACE!
app_name = 'roster'
# Be careful setting the name to just /login use userlogin instead!


urlpatterns = [
    url(r'^roster/$', views.ClubRoster.as_view(), name='club_roster'),

]
