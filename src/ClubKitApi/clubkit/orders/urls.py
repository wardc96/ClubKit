from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'orders'

urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    url(r'^package-create/$', views.order_create_package, name='order_create_package'),
    path('orders/', views.ClubOrders.as_view(), name='orders'),
    path('order/<int:pk>/', views.view_order, name='view_order'),
    path('complete-order/<int:pk>/', views.complete_order, name='complete-order'),
    path('completed-orders/', views.completed_orders, name='completed-orders'),
    path('uncomplete-order/<int:pk>/', views.uncomplete_order, name='uncomplete-order'),
]