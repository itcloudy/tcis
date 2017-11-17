#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:project_tase_case.py
@date:2017/11/15 15:08
"""
from rest_framework import status, permissions
from rest_framework.decorators import list_route
from rest_framework import viewsets
from django.db.models import Count
from project_test.models import ProjectTestCase
from rest_framework.response import Response
from tcis_base.models import User
from ..serializers import *


class ProjectTestCaseViewSet(viewsets.ModelViewSet):
    """
    项目管理
    """
    queryset = ProjectTestCase.objects.all()
    serializer_class = ProjectTestCaseSerializer

