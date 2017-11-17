#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:project_task_type.py
@date:2017/11/15 11:30
"""
from django.db import models


class ProjectTaskType(models.Model):
    """
    任务类型
    """
    name = models.CharField(verbose_name=u"任务类型", max_length=20, unique=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        db_table = "project_task_type"
        verbose_name = u'任务类型'
        verbose_name_plural = u"任务类型管理"
