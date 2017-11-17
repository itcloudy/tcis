#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:project_test_case_history.py
@date:2017/11/15 15:08
"""
from rest_framework import status, permissions
from rest_framework.decorators import list_route
from rest_framework import viewsets
from django.db.models import Count
from project_test.models import ProjectTestCaseHistory
from rest_framework.response import Response
from tcis_base.models import User
from ..serializers import *


class ProjectTestCaseHistoryViewSet(viewsets.ModelViewSet):
    """
    项目管理
    """
    queryset = ProjectTestCaseHistory.objects.all()
    serializer_class = ProjectTestCaseHistorySerializer