from rest_framework import routers
from business.company.views import *

router = routers.DefaultRouter()

router.register(r'company',CompanyViewset,basename='company')
router.register(r'job',JobViewset,basename='job')