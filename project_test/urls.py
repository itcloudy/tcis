#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:urls.py
@date:2017/11/8 10:07
"""
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register(r'project_test', ProjectTestViewSet, 'project_test')
router.register(r'project_test_case', ProjectTestCaseViewSet, 'project_test_case')
router.register(r'project_test_case_history', ProjectTestCaseHistoryViewSet, 'project_test_case_history')
router.register(r'project_test_type', ProjectTestTypeViewSet, 'project_test_type')

urlpatterns = router.urls
