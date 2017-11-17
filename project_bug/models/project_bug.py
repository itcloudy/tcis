#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:project_bug.py
@date:2017/11/8 10:51
"""

from django.db import models


class ProjectBug(models.Model):
    """
    项目bug管理
    """

    STATES = (
        ('draft', u'草稿'),
        ('confirm', u"已确认"),
        ('appointed', u"已指派"),
        ('processing', u"处理中"),
        ('refuse', u"已拒绝"),
        ('hold', u"挂起"),
        ('solved', u"已解决"),
        ('done', u"完成"),
        ('close', u"关闭")
    )
    LEVELS = (
        (1, u"致命"),
        (2, u"重大"),
        (3, u"次要"),
        (4, u"一般"),
        (5, u"建议")
    )
    project = models.ForeignKey("project.Project", verbose_name=u"项目名称")
    task = models.ForeignKey('project.ProjectTask', verbose_name=u"项目任务", null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name=u"Bug名称")
    description = models.TextField(verbose_name=u"Bug描述")
    state = models.CharField(max_length=10, verbose_name=u"状态", choices=STATES, default='draft')
    level = models.IntegerField(verbose_name=u"级别", choices=LEVELS, default=4)
    tester = models.ForeignKey("tcis_base.User", related_name="tester", verbose_name=u"测试员", null=True, blank=True)
    handler = models.ForeignKey("tcis_base.User", related_name="handler", verbose_name=u"处理员", null=True, blank=True)
    checker = models.ForeignKey('tcis_base.User', related_name="checker", verbose_name=u"验证员", null=True, blank=True)
    open_times = models.IntegerField(verbose_name=u"打开次数", default=1)

    class Meta:
        db_table = "project_bug"
        verbose_name = u'项目Bug'
        verbose_name_plural = u"项目Bug管理"

