"""
WatchInSGE System
"""

## @package base.users.views
#
# Views for Wachin Base-users application
# @author Team WatchIn
# @version 1.0.0

from django.contrib.auth.models import (
    User, Group
)

from djoser.views import UserCreateView, UserViewSet
from djoser import signals

from rest_framework import (
    permissions, viewsets, status
)
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .email import AccountCreateEmail


class UserCreateViewApi(UserCreateView):
    """!
    Class that overwrite the class UserCreateView

    @author Leonel P. Hernandez M. (leonelphm at gmail.com)
    @date 03-10-2018
    @version 1.0.0
    """
    serializer_class = CreateUserSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        user = User.objects.get(pk=self.request.user.pk)
        user = serializer.save(fk_user_create=user)
        data = self.request.data
        signals.user_registered.send(
            sender=self.__class__, user=user, request=self.request
        )

        context = {'user': user}
        to = [user.email]
        context = {'user': user, 'password': data['password']}
        AccountCreateEmail(self.request, context).send(to)
