from clubkit.rentapitch import views
from django.urls import path

app_name = 'rentapitch'

urlpatterns = [
    path('', views.PitchRental.as_view(), name='pitch_rental'),
    path('view_bookings/', views.PitchBookings.as_view(), name='pitch_bookings'),
    path('cancel_booking/<int:pk>/', views.cancel_booking, name='cancel_booking'),
    path('edit_booking/<int:pk>/', views.edit_booking, name='edit_booking'),
    path('ajax/load-rental-price/', views.load_pitch_price, name='ajax_load_rental_price'),

]