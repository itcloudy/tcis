#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:test.py
@date:2017/11/15 11:21
"""
from django.db import models


class ProjectTest(models.Model):
    """
    测试用例
    """
    project = models.ForeignKey("project.Project", verbose_name=u"项目名称")
    name = models.CharField(max_length=50, verbose_name=u'测试名称')
    type = models.ForeignKey("ProjectTestType", verbose_name=u"测试类型")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        db_table = "project_test"
        verbose_name = u'测试'
        verbose_name_plural = u"测试管理"
