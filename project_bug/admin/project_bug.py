#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:project_bug.py
@date:2017/11/9 16:23
"""
from django.contrib import admin
from ..models import ProjectBug


@admin.register(ProjectBug)
class ProjectBugAdmin(admin.ModelAdmin):
    """
    项目管理后台
    """
    search_fields = ["project", "name", "handler", "state"]
    list_display = ["project", "name", "handler", "state"]
    list_filter = ['project', "handler", "state", 'tester', 'checker']

