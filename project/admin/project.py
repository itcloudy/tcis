#!/usr/bin/env python
# encoding: utf-8
"""
@project:tcis
@author:cloudy
@site:
@file:project.py
@date:2017/11/9 9:04
"""

from django.contrib import admin
from ..models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    项目管理后台
    """
    list_display = ["name", "manager", "active", "parent", "start_date", "end_date", "parent_left", "parent_right"]

