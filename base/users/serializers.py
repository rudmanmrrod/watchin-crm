"""
WatchInSGE System
"""

## @package base.users.serializers
#
# Serializes the data of the models and data necessary for the api of users
# @author Team WatchIn
# @version 1.0.0

from django.conf import settings
from django.contrib.auth.models import (
    User, Group
)
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from django.db import IntegrityError, transaction

from rest_framework import serializers

from djoser.serializers import UserCreateSerializer

from base.utils.constants import COUNTRY

from .constants import *
from .models import *


class GroupSerializer(serializers.ModelSerializer):    
  """!
  Class to serialize Group Profile model

  @author Leonel P. Hernandez M (leonelphm at gmail.com)
  @date 22-10-2018
  @version 1.0.0
  """

  class Meta:
    model = Group
    fields = ('pk', 'name')


class UserProfileSerializer(serializers.ModelSerializer):
    """!
    Class to serialize User Profile model

    @author Leonel P. Hernandez M (leonelphm at gmail.com)
    @date 22-10-2018
    @version 1.0.0
    """
    fk_job_id = serializers.CharField(write_only=True, allow_blank=True)
    fk_country_id = serializers.CharField(write_only=True, allow_blank=True)

    class Meta:
        model = UserProfile
        fields = ('fk_job', 'fk_country', 'address', 'state',
                  'telephone', 'fk_job_id', 'fk_country_id')
        depth = 1


class CreateUserSerializer(UserCreateSerializer):
    """!
    Class that overwrites the metadata of the class

    @author Ing. Leonel P. Hernandez M. (leonelphm at gmail.com)
    @date 25-09-2018
    @version 1.0.0
    """
    user_profile = UserProfileSerializer(many=False, write_only=True)
    group_id = serializers.CharField(write_only=True)
    groups = GroupSerializer(many=True, read_only=True)
    date_joined = serializers.DateTimeField(format=settings.DATETIME_FORMAT['DATETIME_USER'], read_only=True)
    last_login = serializers.DateTimeField(format=settings.DATETIME_FORMAT['DATETIME_USER'], read_only=True)

    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
          User.USERNAME_FIELD, User._meta.pk.name, 'password',
          'first_name', 'last_name', 'user_profile', 
          'group_id', 'groups', 'is_active',
          'last_login', 'date_joined'
        )
        read_only_fields = ('last_login', 'date_joined',)

    def validate(self, attrs):
        """
        Function that allows to validate the serializer fields
        """
        user = User(attrs.get('password'),
                    attrs.get('username'),
                    attrs.get('first_name'),
                    attrs.get('last_name'),
                    attrs.get('email'))
        password = attrs.get('password')
        group_id = attrs.get('group_id')
        email = attrs.get('email')
        if User.objects.filter(email=email):
          msg = "There is already a user with this email %s" % (email)
          raise serializers.ValidationError({'email': msg})
        try:
          Group.objects.get(pk=group_id)
        except Exception as e:
          raise serializers.ValidationError(
          {'group_id': "This group is not registered"})
        try:
            validate_password(password, user)
        except django_exceptions.ValidationError as e:
            raise serializers.ValidationError({'password': list(e.messages)})
        return attrs

    def create(self, validated_data):
        """
        Function that allows to create a record of the serialized object
        """
        try:
          user = self.perform_create(validated_data)
          user.groups.add(validated_data.get("group_id"))
        except IntegrityError:
          self.fail('cannot_create_user')
        
        fk_user = validated_data.get('user_profile')
        fk_user_create = validated_data.get('fk_user_create')
        
        #: load the value fk_user_create to the OrderedDict
        fk_user['fk_user_create'] = fk_user_create
        
        UserProfile.objects.create(fk_user=user, **fk_user)
        return user

    def perform_create(self, validated_data):
        """
        Function that allows to create object registry User
        """
        with transaction.atomic():
            group_id = validated_data.get('group_id')
            group_name = Group.objects.get(pk=group_id)
            if group_name.name == ADMINS:
              admin = True
            else:
              admin = False
            user = User.objects.create_user(username=validated_data.get(
                      "username"),
                      password=validated_data.get("password"),
                      first_name=validated_data.get("first_name"), 
                      last_name=validated_data.get("last_name"),
                      email=validated_data.get("email"),
                      is_superuser=admin,
                      is_staff=admin,
                      is_active=validated_data.get('is_active'),
                      )
            if settings.DJOSER['SEND_ACTIVATION_EMAIL']:
                user.is_active = False
                user.save(update_fields=['is_active'])
        return user
