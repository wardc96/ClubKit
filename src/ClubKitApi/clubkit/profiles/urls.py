from django.urls import path
from clubkit.profiles import views

# SET THE NAMESPACE!
app_name = 'profiles'

urlpatterns = [
    path('', views.view_profile, name='view_profile'),
    path('edit/', views.edit_profile, name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),
]
