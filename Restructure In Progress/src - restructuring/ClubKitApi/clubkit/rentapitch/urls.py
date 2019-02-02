from django.conf.urls import url
from clubkit.rentapitch import views
from django.urls import path

# SET THE NAMESPACE!
app_name = 'rentapitch'
# Be careful setting the name to just /login use userlogin instead!


urlpatterns = [
    path('', views.PitchRental.as_view(), name='pitch_rental'),
    path('view_bookings/', views.PitchBookings.as_view(), name='pitch_bookings'),
    path('cancel_booking/<int:pk>/', views.cancel_booking, name='cancel_booking'),
    path('edit_booking/<int:pk>/', views.edit_booking, name='edit_booking'),

]