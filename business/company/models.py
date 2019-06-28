"""
WatchInCRM System
"""
## @package business.company.models
#
# Model that builds company data models
# @author Team WatchIn
# @date 23-06-2019
# @version 1.0

from django.db import models

class Company(models.Model):
  """!
  Model class for company data

  @date 23-05-2019
  @version 1.0.0
  """
  ## Company name
  name = models.CharField(max_length=128)
  
  ## Company address
  address = models.CharField(max_length=255)

  ## Company mail
  email = models.EmailField()
  
  ## Company phone
  phone = models.CharField(max_length=25)

  ## Company president
  president = models.CharField(max_length=128)

  def __str__(self):
    return self.name

  class Meta:
    ordering = ("id",)

class Job(models.Model):
  """!
  Model class for jobs data

  @date 23-05-2019
  @version 1.0.0
  """ 
  ## Job name
  name = models.CharField(max_length=50,unique=True)

  ## Job description
  description = models.CharField(max_length=150,unique=True)

  def __str__(self):
    return self.nombre

  class Meta:
    ordering = ("id",)
