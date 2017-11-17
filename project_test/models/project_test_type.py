#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:test_type.py
@date:2017/11/15 11:24
"""
from django.db import models


class ProjectTestType(models.Model):
    """
    测试类型
    """
    name = models.CharField(verbose_name=u"测试类型", max_length=20, unique=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        db_table = "project_test_type"
        verbose_name = u'测试类型'
        verbose_name_plural = u"测试类型"
