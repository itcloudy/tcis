#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:project_meeting.py
@date:2017/11/15 10:48
"""
from django.db import models


class ProjectMeeting(models.Model):
    """
    项目会议
    """
    meeting = models.ForeignKey('tcis_base.TcisMeeting', verbose_name=u"会议")
    project = models.ForeignKey("Project", verbose_name=u"项目")

    class Meta:
        db_table = "project_meeting"
        verbose_name = u'项目会议'
        verbose_name_plural = u"项目会议管理"
