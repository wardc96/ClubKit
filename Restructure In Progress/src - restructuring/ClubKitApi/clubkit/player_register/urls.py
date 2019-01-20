from django.conf.urls import url
from clubkit.player_register import views

# SET THE NAMESPACE!
app_name = 'player_register'
# Be careful setting the name to just /login use userlogin instead!


urlpatterns = [
    url(r'^player_registration/$', views.RegisterPlayer.as_view(), name='player_registration'),

]
