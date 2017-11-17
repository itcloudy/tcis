#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:tcis_meeting.py
@date:2017/11/15 10:51
"""
from django.contrib import admin

from ..models import TcisMeeting


@admin.register(TcisMeeting)
class TcisMeetingAdmin(admin.ModelAdmin):
    """会议管理"""
    list_display = ['title', "moderator", "recorder", 'start_time', 'end_time']
    list_filter = ["moderator", "recorder"]

