from clubkit.player_register import views
from django.urls import path

app_name = 'player_register'

urlpatterns = [
    path('', views.RegisterPlayer.as_view(), name='player_register'),

]
