from clubkit.shop import views
from django.conf.urls import include, url
from django.urls import path


# SET THE NAMESPACE!
app_name = 'shop'
# Be careful setting the name to just /login use userlogin instead!


urlpatterns = [

    path('', views.product_list, name='product_list'),
    path('<category_slug>/', views.product_list, name='product_list_by_category'),
    path('<id>/<slug>/', views.product_detail, name='product_detail'),
    path('', views.ClubShop.as_view(), name='club_shop'),
    path('club_shop_products/', views.ClubShopProducts.as_view(), name='club_shop_products'),
    # path('add_product/', views.add_product, name='add_product'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),
    path('edit_product/<int:pk>/', views.edit_product, name='edit_product'),
    path('club_shop_categories/', views.ClubShopCategories.as_view(), name='club_shop_categories'),
    path('delete_category/<int:pk>/', views.delete_category, name='delete_category'),
    path('edit_category/<int:pk>/', views.edit_category, name='edit_category'),

]




'''
path('', views.product_list, name='product_list'),
    #path('<int:pk>/', views.club_home, name='club_home_with_pk'),
    # path('<int:pk>/', include('clubkit.player_register.urls', namespace='player_registration'), name='club_player_register'),
    #path('edit/', views.edit_club, name='edit_club'),
# url(r'^(?P<pk>\d+)/', include('clubkit.player_register.urls'), name='club_player_register'),
# url(r'^(?P<pk>\d+)/', include('clubkit.roster.urls'), name='club_roster'),
path('(?P<id>\d+)/(?P<slug>[-\w]+)/', views.product_detail, name='product_detail'),
'''

'''
    path('', views.ClubShop.as_view(), name='club_shop'),
    path('club_shop_products/', views.ClubShopProducts.as_view(), name='club_shop_products'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),
    path('edit_product/<int:pk>/', views.edit_product, name='edit_product'),
    path('club_shop_categories/', views.ClubShopCategories.as_view(), name='club_shop_categories'),
    path('delete_category/<int:pk>/', views.delete_category, name='delete_category'),
    path('edit_category/<int:pk>/', views.edit_category, name='edit_category'),
    path('<slug>/', views.product_detail, name='product_detail'),
'''