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

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [

    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^special/', views.special, name='special'),
    url(r'^clubkit/', include('clubkit.api.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),

]
'''
Because we're using viewsets instead of views, we can automatically generate the URL conf for our API, 
by simply registering the viewsets with a router class.
Again, if we need more control over the API URLs we can simply drop down to using regular class-based views, 
and writing the URL conf explicitly.
Finally, we're including default login and logout views for use with the browsable API. That's optional,
but useful if your API requires authentication and you want to use the browsable API.
'''
