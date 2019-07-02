"""WatchInSGE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from djoser.urls import (
    authtoken, urlpatterns
)
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

from base.users.urls import urlpatterns as users_urls

url_djoser_users = urlpatterns + users_urls 

url_djoser_users.pop(1)
url_djoser_users.pop(8)

urlpatterns = [
  path('api/api-auth/', include('rest_framework.urls',
         namespace='rest_framework')),
  path('admin/', admin.site.urls),
  #: Djoser auth And User Create
  path('api/auth/', include(url_djoser_users)),
  #: Sorter urls 
  path('api/utils/', include('base.utils.urls')),
  #: Djoser JWT
  path('api/auth/', include('djoser.urls.jwt')),
]
