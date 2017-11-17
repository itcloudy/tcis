#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:urls.py
@date:2017/11/8 10:06
"""
from django.conf.urls import url
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register(r'project', ProjectViewSet, 'project')
router.register(r'project_task', ProjectTaskViewSet, 'project_task')
router.register(r'project_member', ProjectMemberViewSet, 'project_member')

urlpatterns = router.urls
