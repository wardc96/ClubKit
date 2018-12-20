from django.conf.urls import url
from clubkit.api import views
from django.urls import path
from django.contrib.auth import views as auth_views

# SET THE NAMESPACE!
app_name = 'api'
# Be careful setting the name to just /login use userlogin instead!


urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^club_home/$', views.club_home, name='club_home'),
    url(r'^club_home/edit/$', views.edit_club, name='edit_club'),

]
