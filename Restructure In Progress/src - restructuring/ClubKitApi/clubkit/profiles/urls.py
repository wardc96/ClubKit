from django.conf.urls import url
from clubkit.profiles import views

# SET THE NAMESPACE!
app_name = 'profiles'
# Be careful setting the name to just /login use userlogin instead!


urlpatterns = [
    url(r'^profile', views.view_profile, name='view_profile'),
    # url(r'^profile/$', views.view_profile, name='profile'),
    url(r'^edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),

]
