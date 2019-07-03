"""
WatchInSGE System
"""

## @package base.users.models
#
# Model that builds users data models
# @author Team WatchIn
# @date 23-05-2019
# @version 1.0

from django.contrib.auth.models import User
from django.db import models

from business.company.models import Job
from base.utils.models import (
    Sorter, AbstractBaseModels 
)
from base.utils.constants import COUNTRY


class UserProfile(AbstractBaseModels):
    """!
    Class that contains the profiles of the users

    @author Ing. Leonel P. Hernandez M. (leonelphm at gmail.com)
    @date 17-04-2018
    @version 1.0.0
    """
    fk_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    fk_job = models.ForeignKey(Job, on_delete=models.CASCADE, 
                               null=True, blank=True)
    fk_country = models.ForeignKey(Sorter, on_delete=models.CASCADE,
                                   limit_choices_to={'group_sorter': COUNTRY},
                                   null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    telephone = models.CharField(max_length=20, null=True, blank=True)

    class Meta: 
        """
        Class that builds model metadata
        """
        ordering = ('pk',)
        db_table = 'base_userProfile'

    def __str__(self):
        return self.fk_user.username

