#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:project_task.py
@date:2017/11/8 10:51
"""
from django.db import models


class ProjectTask(models.Model):
    """
    项目任务管理
    """
    STATES = (
        ('draft', u'草稿'),
        ('confirm', u"已确认"),
        ('appointed', u"已指派"),
        ('processing', u"处理中"),
        ('hold', u"挂起"),
        ('done', u"完成")
    )
    LEVELS = (
        (1, u"非常紧急"),
        (2, u"紧急"),
        (3, u"一般"),
        (4, u"次要"),
    )

    project = models.ForeignKey("Project", verbose_name=u"项目")
    type = models.ForeignKey("ProjectTaskType", verbose_name=u"任务类型")
    name = models.CharField(max_length=50, verbose_name=u'项目任务名称', null=True)
    active = models.BooleanField(default=True, verbose_name=u"是否有效")
    description = models.TextField(verbose_name=u"任务描述", null=True, blank=True)
    handler = models.ForeignKey('tcis_base.User', verbose_name=u"处理人", null=True, blank=True)
    parent = models.ForeignKey('self', verbose_name=u"上级任务", null=True, blank=True)
    state = models.CharField(max_length=20, verbose_name=u"状态", choices=STATES, default='draft')
    need_time = models.FloatField(verbose_name=u"估计时长(h)", default=1)
    start_time = models.DateTimeField(verbose_name=u"开始时间", null=True, blank=True)
    end_time = models.DateTimeField(verbose_name=u"计划完成时间", null=True, blank=True)
    real_end_time = models.DateTimeField(verbose_name=u"实际完成时间", null=True, blank=True)
    level = models.IntegerField(verbose_name=u"级别", choices=LEVELS, default=3)

    def __unicode__(self):
        return self.project.name + ":" + self.name

    def __str__(self):
        return self.project.name + ":" + self.name

    class Meta:
        db_table = "project_task"
        verbose_name = u'项目任务'
        verbose_name_plural = u"项目任务管理"
