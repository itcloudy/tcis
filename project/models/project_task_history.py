#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:project_task_history.py
@date:2017/11/15 11:27
"""
from django.db import models


class ProjectTaskHistory(models.Model):
    """
    任务历史
    """
    task = models.ForeignKey("ProjectTask", verbose_name=u"任务")
    description = models.TextField(verbose_name=u"任务描述", null=True, blank=True)
    user = models.ForeignKey("tcis_base.User", verbose_name=u"修改员")

    def __unicode__(self):
        return self.task.name + "(" + self.user.username_zh or self.user.username + ")"

    def __str__(self):
        return self.task.name + "(" + self.user.username_zh or self.user.username + ")"

    class Meta:
        db_table = "project_task_history"
        verbose_name = u'任务历史'
        verbose_name_plural = u"任务历史管理"
