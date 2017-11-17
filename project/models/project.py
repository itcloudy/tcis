#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:project.py
@date:2017/11/8 10:34
"""
from django.db import models
from common import parent_tree


class Project(models.Model):
    """
    项目表
    """
    name = models.CharField(max_length=50, verbose_name=u'项目名称', unique=True, null=False)
    active = models.BooleanField(default=True, verbose_name=u"是否有效")
    start_date = models.DateField(verbose_name=u"开始时间", null=True, blank=True)
    end_date = models.DateField(verbose_name=u"结束时间", null=True, blank=True)
    manager = models.ForeignKey('tcis_base.User', verbose_name=u"项目经理",null=True, blank=True)
    parent_left = models.IntegerField(verbose_name=u"左", unique=True, null=True, blank=True)
    parent_right = models.IntegerField(verbose_name=u"右", unique=True,  null=True, blank=True)
    parent = models.ForeignKey("self", related_name="childs", verbose_name=u"上级项目", null=True, blank=True)
    description = models.TextField(verbose_name=u"项目描述", null=True, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        db_table = "project"
        verbose_name = u'项目'
        verbose_name_plural = u"项目管理"
    
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        obj = parent_tree(self, Project)
        return super(Project, obj).save(force_insert, force_update, using, update_fields)
