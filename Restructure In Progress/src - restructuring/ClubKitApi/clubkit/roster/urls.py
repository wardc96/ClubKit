from django.conf.urls import url
from clubkit.roster import views
from django.urls import path

# SET THE NAMESPACE!
app_name = 'roster'
# Be careful setting the name to just /login use userlogin instead!


urlpatterns = [
    path('', views.ClubRoster.as_view(), name='club_roster'),
    path('delete_roster/<int:pk>/', views.delete_roster, name='delete_roster'),
    path('edit_roster/<int:pk>/', views.edit_roster, name='edit_roster'),
    # url(r'^roster/$', views.ClubRoster.as_view(), name='club_roster'),

]
