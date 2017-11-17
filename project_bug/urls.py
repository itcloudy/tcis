#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:urls.py
@date:2017/11/8 10:06
"""
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register(r'project_bug', ProjectBugViewSet, 'project_bug')

urlpatterns = router.urls
