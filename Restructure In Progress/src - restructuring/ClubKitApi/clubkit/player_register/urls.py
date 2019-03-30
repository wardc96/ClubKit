from django.conf.urls import url
from clubkit.player_register import views
from django.urls import path

# SET THE NAMESPACE!
app_name = 'player_register'
# Be careful setting the name to just /login use userlogin instead!


urlpatterns = [
    path('', views.RegisterPlayer.as_view(), name='player_register'),

]
