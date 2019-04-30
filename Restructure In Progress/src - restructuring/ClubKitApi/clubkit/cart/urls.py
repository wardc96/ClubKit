from django.conf.urls import url
from . import views

app_name = 'cart'

urlpatterns = [
    url(r'^packages/', views.cart_detail_package, name='cart_detail_package'),
    url(r'^packages/add/(?P<package_id>\d+)/$', views.cart_add_package, name='cart_add_package'),
    url(r'^packages/remove/(?P<package_id>\d+)/$', views.cart_remove_package, name='cart_remove_package'),
    url(r'^$', views.cart_detail, name='cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),




]

'''


'''