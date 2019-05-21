from clubkit.clubs import views
from django.urls import path

# SET THE NAMESPACE!
app_name = 'clubs'

urlpatterns = [
    path('', views.club_home, name='club_home'),
    path('<int:pk>/', views.club_home, name='club_home_with_pk'),
    path('edit_club/', views.edit_club, name='edit_club'),
    path('teams/', views.TeamInfo.as_view(), name='teams'),
    path('add_teams/', views.add_team, name='add_teams'),
    path('delete_team/<int:pk>/', views.delete_team, name='delete_team'),
    path('edit_team/<int:pk>/', views.edit_team, name='edit_team'),
    path('pitches/', views.PitchInfo.as_view(), name='pitches'),
    path('add_pitches/', views.add_pitches, name='add_pitches'),
    path('delete_pitch/<int:pk>/', views.delete_pitch, name='delete_pitch'),
    path('edit_pitch/<int:pk>/', views.edit_pitch, name='edit_pitch'),
    path('add_post/', views.ClubAddPosts.as_view(), name='club_post'),
    path('delete_post/<int:pk>/', views.delete_post, name='delete_post'),
    path('edit_post/<int:pk>/', views.edit_post, name='edit_post'),
    path('memberships/', views.Memberships.as_view(), name='memberships'),
    path('add_memberships/', views.add_memberships, name='add_memberships'),
    path('delete_membership/<int:pk>/', views.delete_membership, name='delete_membership'),
    path('edit_membership/<int:pk>/', views.edit_membership, name='edit_membership'),
    path('packages/', views.package_list, name='package_list'),
    # path('packages/<category_slug>/', views.product_list_by_category, name='product_list_by_category'),
    # path('packages/<id>/<slug>/', views.package_detail, name='product_detail'),
     ]
