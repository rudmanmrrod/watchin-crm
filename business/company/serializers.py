from django.db import transaction
from rest_framework import serializers
from .models import *

class CompanySerializers(serializers.ModelSerializer):
  """
  Class to serialize company

  @author Rodrigo Boet (rudmanmrrod at gmail.com)
  @date 23-05-19 (dd-mm-YY)
  @version 1.0
  """
  class Meta:
    model = Company
    fields = '__all__'

  def create(self, validated_data):
    with transaction.atomic():
      company, created = Company.objects.update_or_create(id=1,defaults=validated_data)
    return company

class JobSerializers(serializers.ModelSerializer):
  """
  Class to serialize job

  @author Rodrigo Boet (rudmanmrrod at gmail.com)
  @date 23-05-19 (dd-mm-YY)
  @version 1.0
  """
  class Meta:
    model = Job
    fields = '__all__'