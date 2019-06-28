"""
WatchInCRM System
"""
## @package WachInCRM.routers
#
# Communication routes between views rest services
# @author Team WatchIn
# @date 24-06-2019
# @version 1.0
from rest_framework import routers
from business.company.views import *

router = routers.DefaultRouter()

router.register(r'company',CompanyViewset,basename='company')
router.register(r'job',JobViewset,basename='job')