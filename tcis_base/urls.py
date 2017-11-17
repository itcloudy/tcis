#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:urls.py
@date:2017/11/8 10:07
"""

from django.conf.urls import url
from .views import *
from rest_framework import routers


urlpatterns = [
    url(r'^$', index, name="index"),
]
router = routers.DefaultRouter()

router.register(r'user', UserViewSet, 'user')
router.register(r'group', GroupViewSet, 'group')
router.register(r'permission', PermissionViewSet, 'permission')
urlpatterns += router.urls
