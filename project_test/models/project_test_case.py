#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:test_case.py
@date:2017/11/14 10:30
"""

from django.db import models


class ProjectTestCase(models.Model):
    """
    测试用例
    """
    project = models.ForeignKey("project.Project", verbose_name=u"项目名称")
    task = models.ForeignKey("project.ProjectTask", verbose_name=u"项目任务")
    test = models.ForeignKey("ProjectTest", verbose_name=u"测试")
    name = models.CharField(max_length=100, verbose_name=u"测试用例名称")
    type = models.ForeignKey("ProjectTestType", verbose_name=u"测试类型")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        db_table = "project_test_case"
        verbose_name = u'测试用例'
        verbose_name_plural = u"测试用例"


