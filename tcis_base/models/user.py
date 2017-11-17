#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:user.py
@date:2017/11/8 9:58
"""

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    用户信息扩展
    """
    mobile = models.CharField(max_length=20, verbose_name=u'电话', null=True, blank=True, unique=True, default='')
    short_phone = models.CharField(max_length=10, verbose_name=u'短号', null=True, blank=True, default='')
    username_zh = models.CharField(max_length=20, verbose_name=u'中文名称', null=True, blank=True, default='')
    department = models.ForeignKey('Department', verbose_name=u'部门', null=True, blank=True)
    position = models.ForeignKey("Position", verbose_name=u"职位", null=True, blank=True)

    def __unicode__(self):
        return self.username_zh or self.username

    def __str__(self):
        return self.username_zh or self.username

    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = u'用户管理'



