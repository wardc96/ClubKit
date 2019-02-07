from clubkit.clubs import views
from django.conf.urls import include, url
from django.urls import path


# SET THE NAMESPACE!
app_name = 'clubs'
# Be careful setting the name to just /login use userlogin instead!


urlpatterns = [
    path('', views.club_home, name='club_home'),
    path('<int:pk>/', views.club_home, name='club_home_with_pk'),
    # path('<int:pk>/', include('clubkit.roster.urls', namespace='club_pk'), name='club_pk'),
    path('edit_club/', views.edit_club, name='edit_club'),
    path('teams/', views.TeamInfo.as_view(), name='teams'),
    path('delete_team/<int:pk>/', views.delete_team, name='delete_team'),
    path('edit_team/<int:pk>/', views.edit_team, name='edit_team'),
    path('pitches/', views.PitchInfo.as_view(), name='pitches'),
    path('delete_pitch/<int:pk>/', views.delete_pitch, name='delete_pitch'),
    path('edit_pitch/<int:pk>/', views.edit_pitch, name='edit_pitch'),
    path('add_post/', views.ClubAddPosts.as_view(), name='club_post'),
    path('delete_post/<int:pk>/', views.delete_post, name='delete_post'),
    path('edit_post/<int:pk>/', views.edit_post, name='edit_post'),
    path('memberships/', views.Memberships.as_view(), name='memberships'),
    path('delete_membership/<int:pk>/', views.delete_membership, name='delete_membership'),
    path('edit_membership/<int:pk>/', views.edit_membership, name='edit_membership'),
]

# url(r'^(?P<pk>\d+)/', include('clubkit.player_register.urls'), name='club_player_register'),
# url(r'^(?P<pk>\d+)/', include('clubkit.roster.urls'), name='club_roster'),