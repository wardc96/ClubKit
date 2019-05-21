from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'orders'

urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    url(r'^package-create/$', views.order_create_package, name='order_create_package'),
    path('orders/', views.ClubOrders.as_view(), name='orders'),
]