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
    url(r'^profile/$', views.profile, name='profile'),
]
