#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:project_member.py
@date:2017/11/8 10:59
"""

from django.db import models


class ProjectMember(models.Model):
    """
    项目成员
    """
    project = models.ForeignKey("Project", related_name="members", verbose_name=u"项目")
    member = models.ForeignKey("tcis_base.User", verbose_name=u"项目成员")
    position = models.ForeignKey('tcis_base.Position', verbose_name=u"职位", null=True, blank=True)
    active = models.BooleanField(default=True, verbose_name=u"是否有效")

    def __unicode__(self):
        return self.project.name + ":" + self.member.username_zh

    def __str__(self):
        return self.project.name + ":" + self.member.username_zh

    class Meta:
        unique_together = [("project", "member")]
        db_table = "project_member"
        verbose_name = u'项目成员'
        verbose_name_plural = u"项目成员管理"
