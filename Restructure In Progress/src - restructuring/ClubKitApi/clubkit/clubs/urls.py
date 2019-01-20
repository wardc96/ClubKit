from clubkit.clubs import views
from django.conf.urls import include, url
from django.urls import path


# SET THE NAMESPACE!
app_name = 'clubs'
# Be careful setting the name to just /login use userlogin instead!


urlpatterns = [
    url(r'^', views.club_home, name='club_home'),
    url(r'^(?P<pk>\d+)/', views.club_home, name='club_home_with_pk'),
    # url(r'^(?P<pk>\d+)/', include('clubkit.player_register.urls'), name='club_player_register'),
    # url(r'^(?P<pk>\d+)/', include('clubkit.roster.urls'), name='club_roster'),
    url(r'^edit/$', views.edit_club, name='edit_club'),
]
