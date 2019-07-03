"""
WatchInSGE System
"""

## @package base.utils.urls
#
# Routers for Base-utils Application
# @author Team WatchIn
# @version 1.0.0

from rest_framework.routers import DefaultRouter

from .views import *


router = DefaultRouter(trailing_slash=False)

# base-utils Routers ViewsSets
router.register(r'sorter', SorterGenericViewSet)
router.register(r'sorter-country', SorterCountryViewSet)
router.register(r'sorter-location', SorterLocationViewSet)
router.register(r'sorter-admin', SorterWithOutZoneViewSet)

urlpatterns = router.urls