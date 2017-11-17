#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:group.py
@date:2017/11/13 17:15
"""
from django.contrib.auth.models import Group
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        depth = 2
        fields = "__all__"

