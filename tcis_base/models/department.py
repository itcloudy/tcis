#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:department.py
@date:2017/11/8 10:17
"""
from django.db import models


class Department(models.Model):
    """
    部门管理
    """
    name = models.CharField(max_length=20, verbose_name=u"部门", null=False)
    parent = models.ForeignKey('self', verbose_name=u"上级部门", null=True, blank=True)
    charge = models.ForeignKey('User', related_name='charge', verbose_name=u'负责人', null=True, blank=True)
    description = models.TextField(verbose_name=u"部门职责",null=True, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'部门'
        verbose_name_plural = u'部门管理'