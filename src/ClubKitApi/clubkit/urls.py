"""clubkit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from clubkit.api import views
from django.contrib.auth import views as auth_views


# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [

    path('admin/', admin.site.urls),
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^special/', views.special, name='special'),
    url(r'^account/', include('clubkit.api.urls')),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
'''
Because we're using viewsets instead of views, we can automatically generate the URL conf for our API, 
by simply registering the viewsets with a router class.
Again, if we need more control over the API URLs we can simply drop down to using regular class-based views, 
and writing the URL conf explicitly.
Finally, we're including default login and logout views for use with the browsable API. That's optional,
but useful if your API requires authentication and you want to use the browsable API.
'''
