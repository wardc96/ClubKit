from clubkit.shop import views
from django.conf.urls import include, url
from django.urls import path


# SET THE NAMESPACE!
app_name = 'clubs'
# Be careful setting the name to just /login use userlogin instead!


urlpatterns = [
    path('', views.product_list, name='product_list'),
    #path('<int:pk>/', views.club_home, name='club_home_with_pk'),
    # path('<int:pk>/', include('clubkit.player_register.urls', namespace='player_registration'), name='club_player_register'),
    #path('edit/', views.edit_club, name='edit_club'),
]

# url(r'^(?P<pk>\d+)/', include('clubkit.player_register.urls'), name='club_player_register'),
# url(r'^(?P<pk>\d+)/', include('clubkit.roster.urls'), name='club_roster'),