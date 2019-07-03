"""
WatchInSGE System
"""

## @package base.utils.views
#
# Views for Wachin Base-utils application
# @author Team WatchIn
# @version 1.0.0

import json
from django.conf import settings
from django.contrib.auth.models import (
    User
)
from django.db.models import Q

from rest_framework import (
    viewsets, serializers, 
    status, permissions
)
from rest_framework.response import Response

from .constants import (
    STATE, MUNICIPALITY,
    PARISH, COUNTRY
    )

from .models import *
from .serializers import *
from .mixed import MixedPermissionModelViewSet


class SorterCountryViewSet(MixedPermissionModelViewSet):
    """!
    View to list and create the SorterZona

    @author Ing. Leonel P. Hernandez M. (leonelphm at gmail.com)
    @date 08-10-2018
    @version 1.0.0
    """
    model = Sorter
    queryset = Sorter.objects.filter(group_sorter=COUNTRY)
    serializer_class = SoterCountrySerializer
    permission_classes_by_action = {'create': [permissions.IsAdminUser]}

    def create(self, request):
        """
        Method to create the SorterZona for the user
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(pk=request.user.pk)
        save = serializer.save(fk_user_create=user, group_sorter=COUNTRY)

        return Response(serializer.data)


class SorterLocationViewSet(viewsets.ModelViewSet):
    """!
    View to list the CatalogLocation

    @author Ing. Leonel P. Hernandez M. (leonelphm at gmail.com)
    @date 16-10-2018
    @version 1.0.0
    """
    model = Sorter
    queryset = Sorter.objects.filter(Q(group_sorter=PARISH)|Q(group_sorter=MUNICIPALITY)|Q(group_sorter=STATE)|Q(group_sorter=COUNTRY))
    serializer_class = SoterGenericSerializer
    filter_fields = ('group_sorter',
                     'fk_sorter',
                     'fk_sorter__fk_sorter'
                    )
    http_method_names = ['get']


class SorterGenericViewSet(MixedPermissionModelViewSet):
    """!
    View to create the SorterGeneric

    @author Ing. Leonel P. Hernandez M. (leonelphm at gmail.com)
    @date 16-10-2018
    @version 1.0.0
    """
    model = Sorter
    queryset = Sorter.objects.exclude(Q(group_sorter=PARISH)|Q(group_sorter=MUNICIPALITY)|Q(group_sorter=STATE)|Q(group_sorter=COUNTRY))
    serializer_class = SoterGenericSerializer
    filter_fields = ('group_sorter', 'fk_sorter', 'fk_sorter__fk_sorter')
    permission_classes_by_action = {'create': [permissions.IsAdminUser]}

    def create(self, request):
        """
        Method to create the CatalogZona for the user
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(pk=request.user.pk)
        save = serializer.save(fk_user_create=user)

        return Response(serializer.data)


class SorterWithOutZoneViewSet(viewsets.ModelViewSet):
    """!
    View to manage sorter by admin

    @author Rodrigo Boet (rudmanmrrod at gmail.com)
    @date 01-11-2018
    @version 1.0.0
    """
    model = Sorter
    queryset = Sorter.objects.exclude(
        group_sorter=STATE).exclude(
        group_sorter=MUNICIPALITY).exclude(
        group_sorter=PARISH).exclude(
        group_sorter=COUNTRY)
    serializer_class = SorterWithOutZoneSerializer
    permission_classes = (permissions.IsAdminUser,)

    def create(self, request):
        """
        Method to create the CatalogZona for the user
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(pk=request.user.pk)
        save = serializer.save(fk_user_create=user)

        return Response(serializer.data)

