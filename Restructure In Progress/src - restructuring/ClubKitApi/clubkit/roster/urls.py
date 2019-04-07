from clubkit.roster import views
from django.urls import path

app_name = 'roster'

urlpatterns = [
    path('', views.ClubRoster.as_view(), name='club_roster'),
    path('delete_roster/<int:pk>/', views.delete_roster, name='delete_roster'),
    path('edit_roster/<int:pk>/', views.edit_roster, name='edit_roster'),
]
