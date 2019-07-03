"""
WatchInSGE System
"""

## @package base.utils.serializers
#
# Serializes the data of the models and data necessary for the api of utils
# @author Team WatchIn
# @version 1.0.0

from rest_framework import serializers

from .constants import (
    COUNTRY, STATE,
    MUNICIPALITY, PARISH
    )
from .models import *


class SoterCountrySerializer(serializers.ModelSerializer):
    """!
    Class to serialize Sorter model

    @author Leonel P. Hernandez M (leonelphm at gamil.com)
    @date 08-10-2018
    @version 1.0.0
    """
    fk_sorter_id = serializers.CharField(write_only=True, allow_null=True)

    class Meta:
        model = Sorter
        fields = ("pk", "name_sorter", 'fk_sorter',
                  "group_sorter", "fk_sorter_id")
        read_only_fields = ('group_sorter',)
        depth = 1


    def validate(self, attrs):
        """!
        Method that validates the parameters sent to the serializer

        @param attrs object that contains the values of the serialized fields
        @return attrs object that contains the attributes of the serializer
        """ 
        name_sorter = attrs.get('name_sorter')
        fk_sorter_id = attrs.get('fk_sorter_id')
        if Sorter.objects.filter(group_sorter=COUNTRY, name_sorter=name_sorter):
            msg = "There is already a country with this name"
            raise serializers.ValidationError(msg)
        if fk_sorter_id:
            try:
                Sorter.objects.get(pk=fk_sorter_id, group_sorter=COUNTRY)
            except:
                msg = "This country is not registered"
                raise serializers.ValidationError(msg)
        return attrs


class SoterGenericSerializer(serializers.ModelSerializer):
    """!
    Class to serialize Sorter model

    @author Leonel P. Hernandez M (leonelphm at gamil.com)
    @date 16-10-2018
    @version 1.0.0
    """
    fk_sorter_id = serializers.CharField(write_only=True, allow_null=True)

    class Meta:
        model = Sorter
        fields = ("pk", "name_sorter", 'fk_sorter', 
                  "group_sorter", "fk_sorter_id")
        depth = 1


class SorterWithOutZoneSerializer(SoterGenericSerializer):
    """!
    Class to serialize Sorter model with out zone

    @author Rodrigo Boet (rudmanmrrod at gmail.com)
    @date 01-11-2018
    @version 1.0.0
    """
    def validate(self,attrs):
        """!
        Method to validate serializer

        @param attrs object that contains serializer attributes
        @return attrs object that contains serializer attributes
        """ 
        name_sorter = attrs.get('name_sorter')
        group_sorter = attrs.get('group_sorter')
        if Sorter.objects.filter(group_sorter=group_sorter,
                                 name_sorter=name_sorter):
            msg = "There is already a classifier with that name in this category"
            raise serializers.ValidationError(msg)
        if ((group_sorter == COUNTRY) or (group_sorter == PARISH)
            (group_sorter == STATE) or (group_sorter == MUNICIPALITY)):
            msg = "You are not allowed to register catalogs of this type"
            raise serializers.ValidationError(msg)
        return attrs
