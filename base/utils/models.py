"""
WatchInSGE System
"""
## @package base.utils.models
#
# Model that builds utils data models
# @author Team WatchIn
# @date 23-05-2019
# @version 1.0

from django.contrib.auth.models import User
from django.db import models

from .constants import CATALOG_GROUP_CHOICES


class AbstractBaseModels(models.Model):
    """!
    Class abstract that contains the abstract base

    @author Leonel P. Hernandez M. (leonelphm@gmail.com)
    @date 30-05-2019
    @version 1.0.0
    """
    #: Foreign key of the user that create record
    fk_user_create = models.ForeignKey(User, on_delete=models.CASCADE)
    #: date of modification of the registration
    date_modification =  models.DateTimeField(auto_now=True)
    #: registration date
    date_creation = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Class that builds model metadata
        """
        abstract = True


class Sorter(AbstractBaseModels):
    """!
    Class that contains the data of the Sorter

    @author Leonel P. Hernandez M. (leonelphm@gmail.com)
    @date 04-10-2018
    @version 1.0.0 
    """
    #: Foreign key of the parent sorter
    fk_sorter = models.ForeignKey('self', on_delete=models.CASCADE,
                                  null=True, blank=True)
    #: Name of the classifier
    name_sorter = models.CharField(max_length=256)
    #: Classifier group
    group_sorter = models.CharField(max_length=56, 
                                    choices=CATALOG_GROUP_CHOICES)
    #: Classifier status
    status_sorter = models.BooleanField(default=True)
    
    class Meta:
        """
        Class that builds model metadata
        """
        ordering = ('name_sorter',)
        db_table = 'base_sorter'

    def __str__(self):
        return self.name_sorter
