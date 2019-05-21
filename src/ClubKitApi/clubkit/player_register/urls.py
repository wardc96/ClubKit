from clubkit.player_register import views
from django.urls import path

app_name = 'player_register'

urlpatterns = [
    path('', views.Members.as_view(), name='members'),
    path('delete_member/<int:pk>/', views.delete_member, name='delete_member'),
    path('edit_member/<int:pk>/', views.edit_member, name='edit_member'),
    path('registration', views.RegisterPlayer.as_view(), name='player_register')


]