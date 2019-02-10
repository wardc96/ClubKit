from clubkit.main import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.views.generic.base import TemplateView

# SET THE NAMESPACE!
app_name = 'main'

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    path('our-clubs/', views.OurClubs.as_view(), name='our_clubs'),
    path('our-packages/', views.Packages.as_view(), name='our_packages'),
    path('buy-packages/', views.purchase_packages, name='buy_packages'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


]
