#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:group.py
@date:2017/11/13 17:16
"""
from rest_framework import viewsets
from django.contrib.auth.models import Group
from ..serializers import GroupSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    用户
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

