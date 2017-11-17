#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:meeting_member.py
@date:2017/11/15 11:02
"""
from django.db import models


class MeetingMember(models.Model):
    """
    参会人
    """
    STATES = (
        ('draft', u'通知'),
        ('confirm', u"已知"),
        ('done', u"总结确认")
    )
    meeting = models.ForeignKey('TcisMeeting', related_name='meeting', verbose_name=u"会议")
    user = models.ForeignKey("User", related_name='user', verbose_name=u"参会人")
    state = models.CharField(max_length=20, verbose_name=u"状态", choices=STATES, default='draft')

    def __unicode__(self):
        return self.meeting.name + "(" + self.user.name + ")"

    def __str__(self):
        return self.meeting.name + "(" + self.user.name + ")"

    class Meta:
        verbose_name = u'参会人'
        verbose_name_plural = u'参会人管理'
