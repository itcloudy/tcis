#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:project_member.py
@date:2017/11/9 16:23
"""
from django.contrib import admin
from ..models import ProjectMember


@admin.register(ProjectMember)
class ProjectMemberAdmin(admin.ModelAdmin):
    """
    项目管理后台
    """
    list_display = ["project", "member", "active", "position"]

    fieldsets = [
        (None, {
            'fields': ['project', 'member']})
    ]
