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
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from clubkit.main import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    url('admin/', admin.site.urls),
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^special/', views.special, name='special'),
    url(r'^account/', include('clubkit.main.urls'), name='account'),
    url(r'^profile/', include('clubkit.profiles.urls'), name='profiles'),
    url(r'^club_home/', include('clubkit.clubs.urls'), name='clubs'),
    url(r'^player/', include('clubkit.player_register.urls'), name='player_register'),
    url(r'^roster/', include('clubkit.roster.urls'), name='roster'),
    url(r'^shop/', include('clubkit.shop.urls'), name='shop'),
    url(r'^rent_a_pitch/', include('clubkit.rentapitch.urls'), name='rentapitch'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

