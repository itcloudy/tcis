#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:test_case_history.py
@date:2017/11/15 11:26
"""

from django.db import models


class ProjectTestCaseHistory(models.Model):
    """
    测试用例历史
    """
    case = models.ForeignKey("ProjectTestCase", verbose_name=u"测试用例")
    description = models.TextField(verbose_name=u"任务描述", null=True, blank=True)
    user = models.ForeignKey("tcis_base.User", verbose_name=u"修改员")

    def __unicode__(self):
        return self.case.name + "(" + self.user.username_zh or self.user.username + ")"

    def __str__(self):
        return self.case.name + "(" + self.user.username_zh or self.user.username + ")"

    class Meta:
        db_table = "project_test_case_history"
        verbose_name = u'测试用例历史'
        verbose_name_plural = u"测试用例历史管理"

