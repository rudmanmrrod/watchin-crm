"""
WatchInSEG System
"""
## @package business.company.views
#
# View that controls the processes of the company
# @author Team WatchIn
# @date 24-06-2019
# @version 1.0

from rest_framework import viewsets
from .models import *
from .serializers import *

class CompanyViewset(viewsets.ModelViewSet):
	"""
	View for manage company

	@author Rodrigo Boet (rudmanmrrod at gmail.com)
	@date 23-05-19
	@version 1.0
	"""
	permission_classes = []
	queryset = Company.objects.filter(id=1).all()
	serializer_class = CompanySerializers

class JobViewset(viewsets.ModelViewSet):
	"""
	View for manage jobs

	@author Rodrigo Boet (rudmanmrrod at gmail.com)
	@date 23-05-19
	@version 1.0
	"""
	permission_classes = []
	queryset = Job.objects.all()
	serializer_class = JobSerializers