"""
WatchInSGE System
"""


## @package base.users.urls
#
# Communication routes between views and templates
# @author Team WatchIn
# @date 02-10-2018
# @version 1.0

from django.urls import path

from .views import *

urlpatterns = [
    path(
        'register/users',
        UserCreateViewApi.as_view(),
        name='user-create'
    ),
]