from clubkit.shop import views
from django.conf.urls import include, url
from django.urls import path

# SET THE NAMESPACE!
app_name = 'shop'
# Be careful setting the name to just /login use userlogin instead!


urlpatterns = [
    path('club_shop_products/', views.ClubShopProducts.as_view(), name='club_shop_products'),
    path('club_shop_categories/', views.ClubShopCategories.as_view(), name='club_shop_categories'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),
    path('edit_product/<int:pk>/', views.edit_product, name='edit_product'),

    path('delete_category/<int:pk>/', views.delete_category, name='delete_category'),
    path('edit_category/<int:pk>/', views.edit_category, name='edit_category'),
    path('', views.product_list, name='product_list'),
    path('<category_slug>/', views.product_list, name='product_list_by_category'),
    path('<id>/<slug>/', views.product_detail, name='product_detail'),
    # path('', views.ClubShop.as_view(), name='club_shop'),

    # path('add_product/', views.add_product, name='add_product'),


]



