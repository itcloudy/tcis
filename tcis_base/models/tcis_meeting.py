#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:tcis_meeting.py
@date:2017/11/15 10:50
"""
from django.db import models


class TcisMeeting(models.Model):
    """
    会议
    """
    title = models.CharField(max_length=100, verbose_name=u"会议主题")
    recorder = models.ForeignKey('User', related_name='recorder', verbose_name=u"记录员", null=True, blank=True)
    moderator = models.ForeignKey("User", related_name='moderator', verbose_name=u"主持人",null=True, blank=True)
    start_time = models.DateTimeField(verbose_name=u"开始时间")
    end_time = models.DateTimeField(verbose_name=u"结束时间")

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'会议'
        verbose_name_plural = u'会议管理'
