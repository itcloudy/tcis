#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:meeting_member.py
@date:2017/11/15 11:06
"""
from django.contrib import admin

from ..models import MeetingMember


@admin.register(MeetingMember)
class MeetingMemberAdmin(admin.ModelAdmin):
    """会议管理"""
    list_display = ['meeting', "user", "state"]
    list_filter = ["user", "state"]
